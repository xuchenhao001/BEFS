import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [56.94, 62.98, 70.83, 76.05, 76.88, 79.06, 81.24, 82.02, 82.47, 82.55, 82.88, 82.9, 84.33, 84.25, 83.82, 84.06, 84.49, 85.03, 85.27, 85.81, 85.46, 84.52, 85.22, 84.97, 85.97, 85.94, 85.35, 85.78, 85.73, 86.1, 85.83, 86.08, 85.99, 85.94, 85.83, 86.02, 86.42, 85.65, 85.97, 86.42, 85.89, 86.32, 86.34, 86.45, 86.4, 86.02, 86.77, 86.53, 86.45, 86.05, 86.21, 85.91, 86.67, 86.59, 86.29, 86.37, 86.16, 86.51, 86.21, 86.32, 86.59, 86.29, 86.48, 86.51, 86.34, 86.77, 86.26, 86.08, 86.45, 85.86, 86.88, 86.45, 86.37, 86.4, 86.75, 86.64, 86.24, 86.29, 86.67, 86.59]
fed_sync = [51.53, 67.1, 72.66, 77.5, 81.85, 82.1, 83.33, 83.2, 84.35, 84.41, 84.89, 84.17, 85.11, 85.38, 85.46, 85.08, 84.81, 85.16, 85.08, 84.84, 84.89, 85.11, 85.56, 85.38, 85.46, 85.7, 85.46, 85.4, 85.46, 85.43, 85.08, 85.38, 85.24, 85.19, 85.19, 85.51, 85.51, 85.35, 85.4, 85.7, 85.32, 85.65, 85.62, 85.35, 85.43, 84.97, 85.03, 85.48, 85.19, 85.11, 84.62, 85.11, 85.56, 85.32, 85.19, 85.4, 84.95, 85.05, 85.19, 85.56, 84.97, 84.7, 85.0, 84.95, 84.87, 85.35, 84.68, 85.11, 85.22, 84.84, 85.27, 85.4, 85.51, 85.65, 85.65, 84.97, 85.16, 85.24, 85.7, 85.54]
fed_sync_sgd_1 = [15.0, 15.16, 16.94, 17.53, 19.65, 19.78, 19.84, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78, 19.78]
fed_sync_sgd_01 = [18.87, 19.76, 48.6, 51.51, 37.1, 61.91, 41.8, 50.35, 51.72, 47.47, 42.72, 49.09, 60.62, 64.41, 40.27, 70.7, 33.52, 73.04, 26.75, 35.43, 44.81, 53.25, 59.09, 63.01, 66.69, 69.62, 70.13, 69.49, 69.6, 71.16, 73.44, 74.65, 75.46, 75.91, 75.46, 76.51, 77.28, 77.2, 76.42, 76.4, 76.69, 76.83, 77.1, 77.1, 77.26, 77.23, 77.39, 77.47, 77.42, 77.45, 77.31, 77.23, 77.26, 77.26, 77.31, 77.53, 77.74, 77.85, 77.9, 77.9, 77.9, 77.9, 77.85, 77.85, 77.85, 77.85, 77.85, 77.85, 77.9, 77.9, 77.9, 77.9, 77.9, 77.9, 77.93, 77.88, 77.88, 77.9, 77.93, 77.93]
fed_sync_sgd_001 = [38.47, 51.37, 50.94, 49.01, 49.25, 49.78, 48.52, 47.42, 48.71, 48.17, 51.32, 54.03, 52.26, 55.19, 55.08, 56.1, 51.1, 57.1, 57.63, 58.01, 58.76, 59.19, 59.6, 59.89, 60.16, 59.81, 59.25, 58.63, 58.41, 58.49, 58.33, 58.49, 58.71, 58.71, 58.87, 59.01, 59.09, 59.11, 59.44, 59.38, 59.27, 59.19, 59.19, 59.19, 59.22, 59.25, 59.19, 59.14, 59.19, 59.19, 59.25, 59.22, 59.27, 59.19, 59.19, 59.14, 59.27, 59.3, 59.41, 59.35, 59.35, 59.35, 59.35, 59.35, 59.3, 59.3, 59.33, 59.33, 59.35, 59.35, 59.35, 59.33, 59.35, 59.33, 59.33, 59.3, 59.35, 59.35, 59.3, 59.3]
fed_sync_sgd_0001 = [15.13, 15.05, 15.03, 15.03, 15.08, 15.19, 15.67, 16.32, 17.2, 19.3, 20.99, 22.82, 23.98, 25.13, 26.45, 28.12, 29.54, 30.38, 31.16, 31.24, 31.26, 31.34, 31.4, 31.42, 31.53, 31.56, 31.56, 31.59, 31.61, 31.91, 31.96, 31.99, 32.02, 32.04, 32.18, 32.2, 32.28, 32.28, 32.39, 32.39, 32.39, 32.39, 32.39, 32.39, 32.39, 32.39, 32.39, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45, 32.45]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
