import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [72.12, 77.07, 80.75, 83.12, 84.76, 85.35, 86.59, 86.99, 86.91, 87.53, 87.82, 87.9, 87.88, 88.25, 88.39, 88.79, 88.55, 88.9, 88.63, 88.84, 88.82, 88.82, 88.74, 88.98, 88.66, 88.76, 88.79, 88.63, 88.63, 88.9, 88.74, 88.52, 88.66, 88.63, 88.71, 88.68, 88.9, 88.47, 89.06, 89.27, 88.98, 88.98, 88.84, 89.01, 88.79, 88.84, 88.92, 89.11, 89.11, 89.11, 88.68, 88.79, 88.52, 88.92, 88.71, 88.58, 88.79, 88.76, 88.79, 89.03, 88.66, 89.03, 88.95, 88.68, 88.71, 88.84, 88.76, 88.74, 88.6, 88.92, 89.03, 89.03, 88.82, 89.3, 88.79, 88.84, 88.58, 88.9, 88.74, 89.01]
fed_sync = [62.23, 83.6, 85.51, 87.15, 87.45, 88.01, 88.41, 88.98, 89.01, 89.27, 89.73, 89.3, 89.73, 89.81, 89.78, 90.11, 90.16, 90.27, 90.43, 90.43, 90.51, 90.54, 90.51, 90.43, 90.59, 90.59, 90.54, 90.56, 90.3, 90.59, 90.94, 90.75, 90.73, 90.62, 90.86, 90.4, 90.65, 90.73, 90.65, 90.65, 90.65, 90.35, 90.43, 90.7, 90.91, 90.78, 90.81, 90.86, 90.3, 90.75, 90.48, 90.4, 90.32, 90.86, 90.65, 90.67, 91.13, 90.99, 90.81, 90.75, 91.26, 90.62, 90.91, 90.73, 90.7, 91.08, 90.81, 90.62, 90.48, 90.73, 91.08, 90.75, 90.75, 92.04, 90.97, 90.48, 90.94, 91.37, 90.7, 91.34]
fed_sync_sgd_1 = [13.74, 15.05, 24.57, 31.18, 31.88, 33.12, 34.38, 28.2, 34.44, 36.05, 37.8, 41.56, 48.09, 45.89, 46.99, 46.24, 46.85, 46.4, 46.13, 46.26, 46.67, 46.59, 46.61, 46.69, 46.53, 46.42, 46.42, 46.51, 46.45, 46.72, 46.88, 46.83, 46.77, 46.8, 46.77, 46.77, 46.64, 46.67, 46.61, 46.64, 46.51, 46.51, 46.51, 46.53, 46.64, 46.69, 46.69, 46.64, 46.69, 46.72, 46.69, 46.61, 46.61, 46.69, 46.8, 46.8, 46.72, 46.72, 46.75, 46.75, 46.75, 46.75, 46.75, 46.75, 46.72, 46.69, 46.69, 46.69, 46.69, 46.67, 46.67, 46.67, 46.67, 46.67, 46.64, 46.64, 46.67, 46.67, 46.67, 46.67]
fed_sync_sgd_01 = [20.0, 0.94, 20.0, 0.43, 20.0, 20.38, 20.38, 25.86, 24.81, 26.16, 34.54, 25.91, 37.61, 26.69, 40.56, 29.35, 50.03, 32.77, 50.51, 46.05, 51.1, 51.75, 52.98, 52.96, 53.36, 52.74, 52.77, 52.1, 52.23, 51.4, 52.04, 50.65, 51.59, 50.03, 51.18, 49.87, 50.86, 49.49, 50.81, 50.73, 50.83, 50.81, 50.75, 50.78, 50.75, 50.7, 50.7, 50.65, 50.7, 50.62, 50.56, 50.62, 50.46, 50.48, 50.35, 50.22, 50.13, 50.13, 50.11, 50.08, 50.08, 50.03, 50.0, 50.0, 50.0, 49.89, 49.92, 49.81, 49.81, 49.81, 49.81, 49.81, 49.81, 49.81, 49.81, 49.81, 49.84, 49.84, 49.84, 49.84]
fed_sync_sgd_001 = [21.48, 33.36, 44.78, 46.61, 47.37, 48.39, 49.7, 51.99, 52.42, 55.51, 55.43, 58.04, 57.28, 58.9, 58.41, 59.87, 59.78, 60.59, 60.4, 60.67, 60.78, 60.81, 60.75, 60.83, 60.89, 60.99, 60.81, 60.67, 60.7, 60.97, 61.08, 61.21, 61.29, 61.34, 61.29, 61.26, 61.24, 61.21, 61.32, 61.32, 61.32, 61.32, 61.32, 61.34, 61.37, 61.4, 61.4, 61.4, 61.4, 61.42, 61.42, 61.42, 61.48, 61.48, 61.51, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53, 61.53]
fed_sync_sgd_0001 = [13.2, 14.22, 14.76, 15.48, 17.2, 19.41, 20.91, 21.26, 20.89, 20.59, 20.7, 20.59, 20.19, 20.51, 20.7, 21.05, 20.99, 21.77, 22.02, 22.02, 21.96, 22.04, 22.1, 22.02, 21.99, 22.04, 22.04, 22.15, 22.12, 22.12, 22.12, 22.15, 22.26, 22.2, 22.15, 22.18, 22.12, 22.18, 22.26, 22.26, 22.26, 22.28, 22.28, 22.28, 22.31, 22.31, 22.31, 22.31, 22.31, 22.31, 22.31, 22.31, 22.31, 22.34, 22.37, 22.37, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39, 22.39]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
