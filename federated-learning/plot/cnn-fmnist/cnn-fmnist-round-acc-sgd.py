import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [71.83, 77.42, 81.75, 84.01, 84.54, 84.49, 85.22, 85.48, 85.32, 85.73, 85.56, 85.78, 85.65, 86.21, 86.59, 85.81, 86.24, 86.77, 86.13, 86.48, 86.24, 86.61, 87.02, 87.2, 87.18, 87.31, 86.88, 86.72, 86.91, 87.18, 87.58, 87.26, 87.53, 87.39, 87.42, 87.85, 87.42, 87.9, 86.83, 88.09, 88.09, 86.94, 87.88, 87.74, 87.26, 88.06, 88.44, 88.33, 88.12, 88.17, 88.41, 88.15, 87.9, 87.8, 88.12, 87.39, 88.25, 88.33, 88.04, 88.6, 88.15, 88.15, 88.23, 88.68, 88.12, 88.6, 88.06, 88.52, 88.39, 87.85, 88.12, 88.41, 88.49, 87.93, 88.25, 88.47, 88.55, 88.15, 88.92, 88.79]
fed_sync = [66.77, 71.94, 74.33, 77.5, 78.95, 80.43, 81.05, 82.72, 83.98, 83.87, 84.41, 84.6, 84.97, 85.0, 84.78, 85.54, 85.7, 86.37, 86.13, 85.48, 85.89, 86.32, 86.02, 86.67, 87.04, 86.96, 86.59, 86.48, 86.02, 86.24, 85.97, 86.51, 86.48, 86.4, 86.34, 87.04, 87.26, 86.8, 86.51, 87.15, 87.02, 87.39, 86.67, 86.94, 86.77, 87.23, 86.83, 86.83, 86.42, 86.99, 86.99, 86.69, 86.85, 87.02, 87.26, 87.12, 87.18, 86.77, 87.07, 87.12, 87.15, 86.88, 87.28, 86.91, 86.96, 86.96, 86.56, 87.39, 87.26, 86.94, 86.8, 87.12, 86.88, 87.28, 87.15, 87.12, 87.28, 87.28, 87.55, 87.07]
fed_sync_sgd_1 = [10.51, 14.33, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
fed_sync_sgd_01 = [19.46, 2.42, 22.15, 0.08, 26.16, 0.08, 26.45, 0.19, 25.86, 0.27, 23.9, 0.4, 23.12, 0.56, 20.91, 0.59, 20.89, 1.45, 23.28, 24.81, 26.51, 30.99, 31.83, 39.73, 38.04, 45.81, 42.34, 50.24, 45.35, 51.99, 46.91, 53.68, 48.76, 54.97, 49.87, 55.97, 51.91, 57.66, 53.74, 54.25, 53.6, 53.31, 53.06, 52.96, 52.47, 52.55, 52.47, 52.34, 52.15, 52.02, 52.18, 52.23, 52.18, 52.02, 51.96, 51.94, 51.94, 51.94, 52.12, 52.12, 52.12, 52.12, 52.12, 52.12, 52.12, 52.15, 52.12, 52.15, 52.12, 52.12, 52.1, 52.12, 52.12, 52.12, 52.15, 52.15, 52.18, 52.18, 52.18, 52.18]
fed_sync_sgd_001 = [49.78, 44.35, 54.76, 53.04, 56.48, 59.33, 57.37, 60.51, 57.26, 60.3, 55.27, 57.96, 51.08, 54.89, 49.14, 53.39, 47.69, 51.69, 46.8, 47.26, 46.96, 47.02, 46.99, 47.2, 47.04, 47.04, 46.96, 46.75, 46.72, 46.48, 46.72, 47.02, 47.02, 46.91, 46.85, 46.8, 46.45, 46.45, 46.69, 46.69, 46.69, 46.67, 46.67, 46.67, 46.69, 46.69, 46.67, 46.61, 46.64, 46.67, 46.67, 46.75, 46.72, 46.69, 46.69, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.72, 46.69, 46.69, 46.72, 46.72, 46.72, 46.72, 46.72]
fed_sync_sgd_0001 = [13.82, 17.23, 17.28, 16.42, 17.45, 21.77, 26.77, 28.49, 29.22, 29.89, 30.59, 32.26, 34.38, 37.07, 40.03, 43.39, 46.42, 48.79, 50.86, 50.94, 51.18, 51.26, 51.53, 51.69, 51.94, 51.96, 52.07, 52.23, 52.37, 52.45, 52.58, 52.63, 52.66, 52.82, 52.88, 52.96, 53.09, 53.17, 53.36, 53.41, 53.41, 53.41, 53.41, 53.41, 53.41, 53.44, 53.44, 53.44, 53.47, 53.44, 53.44, 53.41, 53.47, 53.47, 53.47, 53.47, 53.47, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49, 53.49]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
