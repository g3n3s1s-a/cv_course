# Practical 5 - Diffusion Models 

Here is what 1000 reverse diffusion steps look like (figure 1).

<p align="center">
  <img width="444" height="160" src="https://github.com/user-attachments/assets/944df211-2f30-40ff-9d35-b5ffc00ce250" />
  <br>
  <em>Figure 1: 1000 steps.</em>
</p>

When I decrease the number of reverse diffusion steps (figure 2), the generated images become much noisier and it is harder to recognize the digits. This happens because diffusion models rely on gradually removing noise over many small steps. If we use fewer steps, each step has to remove too much noise at once, which leads to poor approximations and lower-quality samples.

<p align="center">
  <img width="446" height="155" src="https://github.com/user-attachments/assets/c323dd43-ed83-4c0e-a1f0-24d7d964713d" />
  <br>
  <em>Figure 2: 500 steps.</em>
</p>

When I increase the number of steps (figure 3 and figure 4), the images may initially improve slightly, but they can also become overly smooth or “thinner.” This happens because the model was trained with a fixed number of timesteps (e.g., 1000), so going beyond could cause a mismatch between training and sampling. The noise schedule is no longer calibrated properly, which can degrade the output.

<p align="center">
  <img width="430" height="159" src="https://github.com/user-attachments/assets/93a58fcd-da03-47f0-b399-4dc6088265ff" />
  <br>
  <em>Figure 3: 1500 steps.</em>
</p>

<p align="center">
  <img width="482" height="181" src="https://github.com/user-attachments/assets/56db572d-bec4-4f30-aa6e-e3d0173d5441" />
  <br>
  <em>Figure 4: 2000 steps.</em>
</p>

To fix this, we could:
- keep the number of steps consistent with training

To increase the probability of generating in-set samples, we can add a classifier. During sampling, we adjust the denoising process to favor outputs that the classifier assigns high probability to being in the dataset. This helps reduce out-of-set samples and improves overall quality.
