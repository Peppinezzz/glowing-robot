import math as m
import cmath as cm
import random
import matplotlib.pyplot as plt


def dft(xs, k):
    arg = lambda n: 2 * m.pi * k * n / len(xs)
    tc = lambda n: m.cos(arg(n)) - m.sin(arg(n)) * 1j
    res_els = [el * tc(i) for i, el in enumerate(xs)]
    return sum(res_els)


def fft(xs, k, lower):
    even_part = dft(xs[1::2], k)
    odd_part = dft(xs[::2], k)
    exp_part = cm.exp(-2 * m.pi * k * 1j / len(xs))
    if lower:
        return even_part + exp_part * odd_part
    else:
        return even_part - exp_part * odd_part


def get_signal(harmonics, time, frequency):
    x = [0 for _ in range(time)]

    for i in range(1, harmonics + 1):
        a = random.random()
        phi = random.random()

        for t in range(time):
            x[t] += a * m.sin(frequency / i * (t + 1) + phi)
    return x


def main():
    harmonics = 8
    time = 1024
    frequency = 100
    nums = get_signal(harmonics, time, frequency)
    dfts = [dft(nums, i) for i in range(len(nums))]
    ffts = [fft(nums, i, True) for i in range(int(len(nums) / 2))] + [
        fft(nums, i, False) for i in range(int(len(nums) / 2), len(nums))
    ]
    dft_reals = [x.real for x in dfts]
    dft_imags = [x.imag for x in dfts]
    fft_reals = [x.real for x in ffts]
    fft_imags = [x.imag for x in ffts]
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 14))
    ax1.plot(range(time), dft_reals)
    ax2.plot(range(time), dft_imags)
    ax3.plot(range(time), fft_reals)
    ax4.plot(range(time), fft_imags)
    plt.show()


if __name__ == '__main__':
    main()
