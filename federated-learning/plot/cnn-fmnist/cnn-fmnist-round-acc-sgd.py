import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [65.94, 75.03, 79.14, 80.91, 82.8, 83.44, 84.11, 84.81, 85.22, 85.38, 84.92, 85.59, 85.62, 86.1, 86.26, 85.3, 86.64, 86.34, 86.53, 85.89, 86.26, 86.16, 85.99, 86.56, 86.13, 86.48, 86.32, 85.97, 86.1, 86.67, 86.32, 86.29, 86.64, 86.05, 86.26, 86.26, 86.8, 86.75, 86.8, 86.94, 86.53, 86.02, 86.16, 87.12, 86.83, 86.69, 86.99, 86.83, 86.21, 86.91, 86.64, 86.61, 86.72, 86.64, 86.77, 87.39, 87.42, 86.67, 87.28, 87.02, 87.1, 86.88, 86.56, 87.07, 86.85, 87.15, 86.96, 87.28, 87.63, 87.07, 87.26, 87.74, 87.37, 86.64, 87.47, 87.42, 87.04, 87.45, 87.5, 87.26]
fed_sync = [66.72, 75.81, 79.89, 81.48, 82.74, 84.03, 84.57, 84.97, 85.11, 85.19, 85.0, 85.46, 85.3, 85.81, 85.81, 85.73, 85.7, 86.05, 86.05, 86.16, 85.59, 85.67, 85.97, 85.91, 85.89, 85.94, 86.05, 86.02, 85.94, 86.13, 86.16, 86.13, 86.24, 85.94, 85.67, 86.16, 85.91, 85.73, 85.89, 86.05, 86.08, 85.67, 85.62, 86.02, 85.86, 85.81, 85.89, 85.62, 85.78, 86.13, 85.94, 86.08, 86.08, 86.02, 85.65, 86.72, 86.02, 86.05, 86.16, 86.53, 86.05, 86.51, 86.21, 86.21, 85.81, 85.62, 86.24, 85.67, 85.89, 86.08, 86.37, 86.21, 86.4, 86.02, 86.29, 86.59, 85.97, 86.56, 86.13, 85.97]
fed_sync_sgd = [12.53, 28.9, 30.91, 33.12, 36.53, 18.74, 42.77, 21.67, 22.34, 27.5, 24.41, 36.94, 29.41, 51.1, 26.94, 48.68, 31.91, 52.02, 31.37, 14.84, 17.61, 26.61, 29.09, 55.19, 54.84, 47.88, 55.16, 18.47, 59.78, 37.15, 40.56, 38.28, 39.92, 47.55, 49.7, 46.59, 57.39, 53.58, 59.81, 49.33, 21.56, 48.49, 37.98, 51.48, 55.65, 61.85, 53.06, 45.97, 45.89, 55.19, 51.77, 48.28, 31.13, 66.85, 50.59, 47.96, 64.41, 56.16, 64.25, 73.39, 55.11, 36.16, 46.42, 54.09, 69.03, 56.32, 60.91, 63.82, 46.24, 47.93, 62.85, 62.9, 65.78, 69.81, 67.47, 60.24, 52.42, 62.66, 70.24, 49.14]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")
