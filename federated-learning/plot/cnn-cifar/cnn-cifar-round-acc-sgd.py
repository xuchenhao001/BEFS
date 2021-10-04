import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [23.6, 31.91, 38.9, 42.47, 43.63, 44.76, 46.24, 46.88, 46.75, 45.99, 47.12, 46.51, 46.53, 46.85, 47.28, 46.8, 46.67, 46.32, 47.18, 46.91, 46.94, 47.1, 47.18, 47.07, 47.04, 47.42, 47.1, 47.15, 48.12, 47.82, 47.66, 47.61, 46.88, 46.88, 46.77, 47.02, 47.42, 46.94, 46.91, 47.1, 46.94, 47.02, 46.88, 46.51, 46.77, 47.04, 46.1, 47.23, 47.39, 46.85, 46.77, 46.96, 46.61, 46.53, 46.53, 47.1, 46.59, 47.23, 47.1, 46.64, 46.77, 46.64, 47.04, 46.56, 46.61, 46.91, 46.45, 47.31, 46.72, 46.53, 46.67, 46.48, 46.56, 46.88, 47.39, 46.85, 45.91, 46.51, 47.12, 47.15, 47.12, 46.72, 46.91, 46.59, 46.88, 46.26, 45.75, 46.61, 46.32, 46.77, 46.18, 46.67, 47.15, 46.4, 46.59, 46.18, 46.02, 46.16, 45.83, 46.42]
fed_sync = [28.76, 34.6, 37.2, 40.19, 44.49, 44.89, 47.47, 48.23, 47.72, 48.39, 49.06, 48.44, 49.11, 48.9, 49.01, 48.95, 48.55, 48.76, 49.01, 48.9, 49.54, 49.65, 49.81, 49.68, 49.81, 49.84, 49.87, 49.78, 50.08, 50.08, 49.62, 49.33, 49.87, 50.27, 49.46, 49.6, 49.17, 49.41, 50.03, 49.73, 49.06, 49.11, 49.6, 48.92, 49.68, 49.01, 49.62, 49.57, 49.33, 49.49, 49.09, 49.33, 48.49, 49.01, 49.19, 48.68, 48.76, 49.09, 48.66, 48.31, 48.47, 48.71, 49.7, 48.95, 49.68, 48.82, 49.57, 48.74, 48.44, 49.84, 49.06, 49.11, 49.17, 48.98, 48.87, 48.87, 49.19, 48.9, 48.66, 48.76, 48.41, 48.68, 48.87, 48.84, 49.17, 48.68, 48.36, 48.68, 48.79, 49.22, 49.17, 49.7, 48.79, 49.41, 49.03, 49.3, 48.9, 48.49, 49.11, 49.01]
fed_sync_sgd_1 = [18.58, 15.03, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0]
fed_sync_sgd_01 = [21.08, 20.97, 21.29, 21.67, 22.12, 25.05, 27.66, 28.92, 30.3, 32.47, 34.46, 35.54, 35.97, 36.29, 36.24, 36.67, 36.45, 36.69, 36.94, 36.91, 36.75, 36.61, 36.56, 36.96, 36.88, 37.07, 37.1, 37.12, 37.1, 37.2, 37.39, 37.15, 37.12, 37.31, 37.42, 37.53, 37.45, 37.58, 37.39, 37.37, 37.39, 37.37, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.37, 37.37, 37.37, 37.34, 37.31, 37.28, 37.28, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.34, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31, 37.31]
fed_sync_sgd_001 = [17.5, 17.82, 21.56, 25.54, 26.53, 27.12, 27.23, 27.42, 27.42, 27.61, 27.74, 28.06, 28.58, 28.66, 29.01, 29.17, 28.98, 28.92, 29.22, 29.19, 29.09, 28.98, 28.92, 28.9, 28.95, 28.98, 29.03, 29.09, 29.03, 29.06, 29.14, 29.17, 29.3, 29.35, 29.33, 29.38, 29.44, 29.49, 29.52, 29.52, 29.52, 29.46, 29.46, 29.46, 29.52, 29.52, 29.52, 29.52, 29.52, 29.52, 29.52, 29.49, 29.49, 29.49, 29.49, 29.49, 29.49, 29.52, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46, 29.46]
fed_sync_sgd_0001 = [7.12, 7.12, 7.15, 7.04, 6.99, 6.99, 6.94, 6.83, 6.8, 6.88, 6.94, 6.99, 7.15, 7.45, 7.77, 8.09, 8.68, 9.52, 10.51, 10.67, 10.75, 10.86, 11.02, 11.13, 11.24, 11.21, 11.34, 11.56, 11.72, 11.83, 11.88, 11.99, 12.07, 12.12, 12.23, 12.34, 12.42, 12.47, 12.66, 12.66, 12.74, 12.77, 12.77, 12.85, 12.85, 12.85, 12.85, 12.9, 12.9, 12.88, 12.88, 12.88, 12.9, 12.9, 12.93, 12.93, 12.93, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.96, 12.93, 12.93, 12.93, 12.93, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98, 12.98]


save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
