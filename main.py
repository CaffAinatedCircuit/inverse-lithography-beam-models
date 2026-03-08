# main.py

import os
import torch
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from config import CONFIG
from gds_utils import load_gds_layers, rasterize
from models import LocalizedModel, EwaldModel
from trainer import train_model, save_loss_curve
from metrics import compute_metrics

device = torch.device(CONFIG["device"])

os.makedirs("images", exist_ok=True)
os.makedirs("results", exist_ok=True)

sns.set(style="whitegrid")

for gds_file in os.listdir("gds"):

    if not gds_file.endswith(".gds"):
        continue

    print(f"\nProcessing GDS: {gds_file}")

    gds_path = os.path.join("gds", gds_file)
    cell, layers = load_gds_layers(gds_path)

    for layer in layers:

        print(f"\nLayer: {layer}")

        target = rasterize(cell, layer, CONFIG["resolution"]).to(device)
        if target is None:
            continue
        base_name = f"{gds_file.replace('.gds','')}_{layer}"

        # Save original
        plt.imsave(f"images/{base_name}_original.png",
                   target.cpu().numpy(), cmap="gray")

        results_df = []

        for beams in CONFIG["beam_counts"]:

            print(f"\nBeams: {beams}")

            # Localized
            model_local = LocalizedModel(CONFIG["resolution"], beams)
            model_local, hist_local = train_model(
                model_local, target,
                CONFIG["epochs"],
                CONFIG["learning_rate"],
                device
            )

            pred_local = model_local()
            mse_l, ssim_l, edge_l, spec_l = compute_metrics(pred_local, target)

            save_loss_curve(hist_local,
                            f"results/{base_name}_localized_{beams}_loss.png")

            # Ewald
            model_ewald = EwaldModel(CONFIG["resolution"], beams, CONFIG["k0"])
            model_ewald, hist_ewald = train_model(
                model_ewald, target,
                CONFIG["epochs"],
                CONFIG["learning_rate"],
                device
            )

            pred_ewald = model_ewald()
            mse_e, ssim_e, edge_e, spec_e = compute_metrics(pred_ewald, target)

            save_loss_curve(hist_ewald,
                            f"results/{base_name}_ewald_{beams}_loss.png")

            # Save side-by-side visualization
            plt.figure(figsize=(12,6))

            plt.subplot(2,3,1)
            plt.imshow(target.cpu(), cmap="gray")
            plt.title("Original")

            plt.subplot(2,3,2)
            plt.imshow(pred_local.detach().cpu(), cmap="inferno")
            plt.title("Localized")

            plt.subplot(2,3,3)
            plt.imshow(torch.abs(pred_local-target).detach().cpu(), cmap="hot")
            plt.title("Localized Error")

            plt.subplot(2,3,5)
            plt.imshow(pred_ewald.detach().cpu(), cmap="inferno")
            plt.title("Ewald")

            plt.subplot(2,3,6)
            plt.imshow(torch.abs(pred_ewald-target).detach().cpu(), cmap="hot")
            plt.title("Ewald Error")

            plt.tight_layout()
            plt.savefig(f"images/{base_name}_{beams}_comparison.png", dpi=300)
            plt.close()

            results_df.append([
                beams, "localized", mse_l, ssim_l, edge_l, spec_l
            ])
            results_df.append([
                beams, "ewald", mse_e, ssim_e, edge_e, spec_e
            ])

        df = pd.DataFrame(results_df,
                          columns=["Beams","Model","MSE","SSIM","EdgeOverlap","SpectralMatch"])

        df.to_csv(f"results/{base_name}_metrics.csv", index=False)

        # -------- Summary Graphs --------

        for metric in ["MSE","SSIM","EdgeOverlap","SpectralMatch"]:

            plt.figure(figsize=(6,4))
            sns.lineplot(data=df, x="Beams", y=metric, hue="Model", marker="o")
            plt.title(f"{metric} vs Beam Count")
            plt.tight_layout()
            plt.savefig(f"results/{base_name}_{metric}_vs_beams.png", dpi=300)
            plt.close()

print("\nALL TRAINING COMPLETED SUCCESSFULLY.")