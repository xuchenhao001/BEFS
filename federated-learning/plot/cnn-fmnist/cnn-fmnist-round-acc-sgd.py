import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [72.34, 76.24, 79.87, 82.61, 83.98, 85.27, 85.83, 86.13, 86.59, 86.96, 86.4, 86.61, 86.56, 86.96, 86.88, 87.04, 87.2, 86.96, 87.39, 87.53, 87.37, 87.5, 87.77, 87.61, 87.58, 87.96, 87.66, 87.39, 87.47, 87.66, 87.58, 87.58, 87.37, 87.45, 87.61, 87.66, 87.5, 87.66, 87.55, 87.31, 87.42, 87.66, 87.63, 87.58, 87.85, 87.5, 87.72, 87.61, 87.61, 87.61]
fed_sync = [65.3, 74.49, 78.25, 79.33, 80.03, 80.65, 80.7, 80.75, 81.42, 81.32, 81.48, 81.72, 81.56, 81.48, 82.1, 81.91, 82.69, 82.28, 82.26, 82.31, 83.17, 82.2, 82.9, 82.9, 83.31, 82.9, 82.98, 82.72, 83.06, 83.55, 83.63, 83.52, 83.92, 84.22, 84.35, 84.6, 83.9, 83.49, 83.66, 83.92, 84.19, 83.74, 83.68, 84.11, 83.76, 84.11, 83.74, 83.71, 83.98, 84.14]
fed_sync_sgd = [23.15, 12.5, 15.0, 12.5, 10.05, 16.83, 49.22, 37.12, 48.09, 41.21, 55.78, 32.2, 50.48, 50.24, 40.78, 53.82, 56.85, 48.17, 51.51, 52.45, 55.11, 59.87, 51.53, 55.99, 55.32, 43.74, 57.45, 51.53, 55.3, 30.22, 47.39, 45.67, 39.49, 40.78, 47.96, 26.37, 47.8, 25.48, 45.67, 27.07, 38.76, 29.44, 42.66, 25.67, 49.62, 26.21, 59.14, 30.99, 58.95, 31.64]

fed_avg = [67.28, 72.2, 77.58, 81.34, 82.72, 83.47, 85.89, 85.62, 85.83, 86.4, 86.18, 85.97, 86.69, 87.12, 86.72, 86.59, 86.56, 87.1, 87.26, 87.07, 86.59, 87.31, 87.02, 86.64, 87.55, 87.2, 86.53, 87.07, 87.15, 87.2, 87.12, 87.12, 87.37, 87.45, 87.39, 87.34, 87.34, 87.1, 87.45, 87.45, 87.37, 87.53, 87.72, 87.8, 87.1, 87.53, 87.85, 87.47, 87.66, 87.85]
fed_sync = [62.45, 71.61, 77.85, 80.13, 82.8, 84.01, 85.19, 85.38, 85.32, 85.83, 85.78, 85.89, 86.37, 87.07, 86.13, 86.75, 86.02, 86.64, 87.2, 87.47, 86.72, 87.37, 86.94, 86.75, 87.42, 87.28, 87.53, 87.45, 88.12, 87.61, 87.74, 87.42, 87.72, 87.42, 87.74, 87.23, 87.45, 87.58, 87.77, 87.88, 87.47, 87.82, 87.66, 88.12, 88.12, 87.96, 87.66, 87.82, 88.09, 87.88]
fed_sync_sgd = [10.27, 18.49, 21.48, 22.98, 26.26, 30.3, 32.12, 33.52, 34.6, 35.97, 36.8, 36.99, 37.28, 37.82, 38.25, 38.71, 39.19, 39.35, 39.54, 40.0, 40.35, 41.08, 41.02, 41.13, 40.99, 40.99, 41.21, 41.29, 41.64, 42.18, 42.15, 41.96, 41.75, 42.04, 41.83, 41.8, 41.85, 41.77, 41.88, 41.91, 41.8, 41.72, 41.96, 41.88, 41.94, 41.96, 41.94, 41.96, 42.28, 42.28]


save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")