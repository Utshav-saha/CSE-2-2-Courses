# Sampling: 10 Python lab problems

Each folder is an independent 30-minute practice exam and contains:
- statement.pdf: one-page problem statement, concepts, contracts, and example.
- template.py: TODO functions plus a ready-to-run printing/plotting driver.
- solution.py: complete reference solution using the same driver.

Scope: physical PDF pages 1-27 of Lecture 5 - Sampling.pdf, ending with ideal sinc interpolation. ZOH, linear interpolation, and the later DFT section are excluded. No FFT is needed.

Requirements: Python 3, NumPy, Matplotlib. Install with `python -m pip install numpy matplotlib` if needed. Open a problem folder and run `python template.py` after completing its TODOs. An untouched template intentionally raises NotImplementedError. Run `python solution.py` to check the reference afterward; close the plot window to finish. All data are embedded; no keyboard input is required.

The 30-minute limit applies to EACH problem. Easy problems leave more time for checking; hard problems combine concepts but include supporting helpers. Drivers and plot formatting are supplied so time is spent on sampling computations. PDF statements contain mathematical definitions and requirements, not coding walkthroughs.

Use physical PDF page numbers, not the smaller slide numbers printed inside the lecture. All frequencies are in Hz except problems 05 and 07, which explicitly use rad/s. Sinc is normalized. Finite sinc sums are approximations between sample instants, not exact infinite-sample recovery.

## Problems
01. Easy: Uniform sampling of a sinusoid
02. Easy: Choose a safe sampling rate
03. Easy: Different signals, identical samples
04. Easy: The ideal interpolation pulse
05. Medium: Build the sampled spectrum
06. Medium: Where do cosine frequencies fold?
07. Medium: Recover the central spectral copy
08. Medium: Reconstruct from a finite sample set
09. Hard: When several tones become one
10. Hard: More samples or a higher sampling rate?
