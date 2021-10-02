import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [38.58, 48.28, 60.81, 65.22, 67.5, 69.01, 70.03, 71.51, 72.12, 72.58, 73.23, 73.92, 74.27, 74.38, 74.76, 75.16, 75.4, 75.51, 76.02, 76.18, 76.26, 76.61, 76.77, 76.85, 76.85, 77.07, 77.37, 77.18, 77.5, 77.63, 77.61, 77.98, 77.96, 77.9, 77.74, 78.06, 78.06, 78.17, 78.25, 78.17, 78.49, 77.93, 78.28, 78.12, 78.47, 78.33, 78.15, 78.52, 78.55, 78.66]
fed_sync = [46.4, 54.22, 59.35, 63.71, 65.27, 66.1, 66.94, 67.55, 67.82, 68.39, 69.35, 70.16, 70.51, 70.99, 71.13, 71.67, 72.45, 72.5, 72.88, 73.66, 73.87, 74.38, 74.73, 75.32, 75.67, 75.78, 76.32, 76.42, 76.61, 76.8, 77.1, 76.96, 77.07, 77.28, 77.5, 77.77, 77.69, 77.61, 78.15, 78.23, 77.9, 78.17, 78.2, 78.47, 78.71, 79.06, 78.55, 78.9, 79.11, 78.98]
fed_sync_sgd = [42.34, 46.32, 47.93, 43.2, 44.46, 48.47, 48.15, 49.25, 52.66, 48.41, 57.45, 50.3, 56.26, 49.81, 56.34, 50.46, 58.25, 47.82, 58.68, 48.31, 59.25, 48.92, 57.96, 50.59, 58.98, 51.05, 57.42, 52.74, 57.23, 50.89, 58.66, 46.37, 59.46, 46.37, 60.35, 45.19, 61.59, 44.62, 62.55, 43.58, 62.72, 42.31, 64.01, 42.45, 65.0, 42.18, 64.65, 41.83, 64.92, 42.42]

fed_avg = [45.27, 57.61, 63.25, 66.24, 69.7, 72.26, 73.36, 74.11, 75.16, 75.48, 76.1, 76.34, 76.59, 76.77, 77.39, 77.93, 78.23, 78.52, 78.41, 78.76, 78.74, 79.38, 79.33, 79.33, 79.22, 79.22, 79.49, 79.87, 79.95, 79.97, 80.05, 80.32, 80.19, 80.62, 80.32, 80.65, 80.62, 80.91, 80.81, 80.81, 81.02, 80.99, 80.99, 80.97, 81.59, 81.94, 81.53, 81.83, 81.94, 81.77]
fed_sync = [54.38, 60.94, 65.59, 68.6, 70.0, 70.24, 70.83, 71.51, 72.23, 72.53, 72.96, 73.52, 73.82, 74.03, 74.78, 75.05, 75.7, 75.91, 76.69, 77.28, 77.53, 78.17, 78.58, 79.14, 79.09, 79.68, 79.81, 79.92, 80.24, 80.62, 80.32, 80.56, 80.7, 80.67, 80.86, 80.97, 81.21, 81.29, 81.61, 81.53, 81.59, 81.51, 81.42, 81.72, 81.56, 81.8, 81.67, 81.91, 81.96, 81.77]
fed_sync_sgd = [10.03, 11.59, 13.2, 15.05, 17.47, 21.13, 23.87, 25.78, 27.63, 29.09, 30.0, 31.16, 31.8, 32.96, 33.66, 34.44, 35.24, 35.86, 36.64, 37.34, 38.39, 39.11, 39.62, 40.03, 40.43, 41.05, 41.48, 42.31, 42.93, 43.63, 44.03, 44.41, 44.68, 45.08, 45.27, 45.48, 45.86, 46.21, 46.64, 46.91, 47.2, 47.47, 47.5, 47.74, 48.04, 48.2, 48.47, 48.71, 48.71, 48.76]


save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")