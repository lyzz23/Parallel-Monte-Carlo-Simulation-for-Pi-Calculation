import numpy as np
import matplotlib.pyplot as plt
import threading


def estimate_pi_segment(start, end, points, results, index):
    inside_circle = 0
    for i in range(start, end):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    results[index] = inside_circle


def estimate_pi(num_points, num_threads):
    points_per_thread = num_points // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start = i * points_per_thread
        end = start + points_per_thread
        thread = threading.Thread(target=estimate_pi_segment, args=(start, end, num_points, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_inside_circle = sum(results)
    pi_estimate = 4 * total_inside_circle / num_points
    return pi_estimate


def plot_points(x, y, inside_circle):
    plt.figure(figsize=(8, 8))
    plt.scatter(x[:inside_circle], y[:inside_circle], color='blue', s=1, label='Inside Circle')
    plt.scatter(x[inside_circle:], y[inside_circle:], color='red', s=1, label='Outside Circle')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Monte Carlo Estimation of Pi')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def main():
    num_points = 1000000  # 数据点数量
    num_threads = 4  # 使用的线程数

    pi_estimate = estimate_pi(num_points, num_threads)

    print(f"Estimated value of Pi: {pi_estimate}")

    # 可视化结果
    x = np.random.uniform(0, 1, num_points)
    y = np.random.uniform(0, 1, num_points)
    inside_circle = np.sum(x ** 2 + y ** 2 <= 1)
    plot_points(x, y, inside_circle)


if __name__ == "__main__":
    main()
