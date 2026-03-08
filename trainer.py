# trainer.py

import torch
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

sns.set(style="whitegrid")

def train_model(model, target, epochs, lr, device):

    model = model.to(device)
    target = target.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = torch.nn.MSELoss()

    history = []

    print("Training started...")
    for epoch in tqdm(range(epochs), desc="Epoch Progress"):

        optimizer.zero_grad()
        pred = model()
        loss = loss_fn(pred, target)
        loss.backward()
        optimizer.step()

        history.append(loss.item())

    return model, history


def save_loss_curve(history, path):
    plt.figure(figsize=(6,4))
    plt.plot(history, linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.title("Epoch-wise Loss")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()