# models.py

import torch
import torch.nn as nn
import numpy as np

class LocalizedModel(nn.Module):

    def __init__(self, resolution, num_beams):
        super().__init__()

        self.num_beams = num_beams

        x = torch.linspace(-1,1,resolution)
        y = torch.linspace(-1,1,resolution)

        X, Y = torch.meshgrid(x,y,indexing='ij')

        self.register_buffer("X", X)
        self.register_buffer("Y", Y)

        self.kx = nn.Parameter(torch.randn(num_beams)*10)
        self.ky = nn.Parameter(torch.randn(num_beams)*10)

        self.real = nn.Parameter(torch.randn(num_beams)*0.1)
        self.imag = nn.Parameter(torch.randn(num_beams)*0.1)

        self.x0 = nn.Parameter(torch.rand(num_beams)*2 - 1)
        self.y0 = nn.Parameter(torch.rand(num_beams)*2 - 1)
        self.log_sigma = nn.Parameter(torch.zeros(num_beams))

    def forward(self):
        E = 0
        for i in range(self.num_beams):
            sigma = torch.exp(self.log_sigma[i]) + 1e-3
            envelope = torch.exp(
                -((self.X-self.x0[i])**2 + (self.Y-self.y0[i])**2)/(sigma**2)
            )
            coeff = torch.complex(self.real[i], self.imag[i])
            phase = self.kx[i]*self.X + self.ky[i]*self.Y
            E += coeff * torch.exp(1j*phase) * envelope
        return torch.abs(E)**2


class EwaldModel(nn.Module):

    def __init__(self, resolution, num_beams, k0):
        super().__init__()

        self.num_beams = num_beams
        self.k0 = k0

        x = torch.linspace(-1,1,resolution)
        y = torch.linspace(-1,1,resolution)

        X, Y = torch.meshgrid(x,y,indexing='ij')

        self.register_buffer("X", X)
        self.register_buffer("Y", Y)

        self.theta = nn.Parameter(torch.rand(num_beams)*2*np.pi)

        self.real = nn.Parameter(torch.randn(num_beams)*0.1)
        self.imag = nn.Parameter(torch.randn(num_beams)*0.1)

        self.x0 = nn.Parameter(torch.rand(num_beams)*2 - 1)
        self.y0 = nn.Parameter(torch.rand(num_beams)*2 - 1)
        self.log_sigma = nn.Parameter(torch.zeros(num_beams))

    def forward(self):
        E = 0
        for i in range(self.num_beams):
            kx = self.k0 * torch.cos(self.theta[i])
            ky = self.k0 * torch.sin(self.theta[i])

            sigma = torch.exp(self.log_sigma[i]) + 1e-3
            envelope = torch.exp(
                -((self.X-self.x0[i])**2 + (self.Y-self.y0[i])**2)/(sigma**2)
            )

            coeff = torch.complex(self.real[i], self.imag[i])
            phase = kx*self.X + ky*self.Y
            E += coeff * torch.exp(1j*phase) * envelope

        return torch.abs(E)**2