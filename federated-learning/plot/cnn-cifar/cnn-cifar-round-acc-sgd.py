import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [21.32, 31.67, 37.53, 40.78, 43.44, 45.43, 48.15, 48.68, 49.68, 50.56, 51.48, 51.1, 50.4, 50.67, 50.65, 50.83, 51.34, 50.94, 50.78, 50.83, 50.78, 50.91, 50.65, 50.48, 50.81, 50.7, 50.3, 49.6, 49.68, 50.05, 50.32, 49.84, 49.87, 49.95, 49.89, 50.3, 50.03, 49.65, 49.65, 49.73, 49.33, 49.87, 49.68, 49.54, 49.6, 49.33, 49.78, 50.0, 49.49, 50.38, 49.68, 50.7, 49.44, 49.95, 49.81, 50.19, 49.19, 49.57, 49.76, 50.03, 50.32, 50.11, 50.3, 50.32, 49.68, 49.49, 49.38, 49.3, 49.19, 49.46, 49.52, 49.14, 49.7, 49.78, 48.87, 49.52, 49.62, 49.7, 49.95, 49.97]
fed_sync = [22.5, 29.76, 33.52, 38.58, 42.8, 43.15, 44.78, 46.59, 47.58, 48.66, 48.39, 49.14, 49.97, 49.95, 51.08, 51.18, 50.91, 50.78, 50.46, 51.32, 51.69, 51.45, 51.29, 51.16, 50.89, 51.05, 51.16, 50.7, 50.19, 50.81, 50.3, 50.3, 50.56, 50.54, 50.43, 50.62, 49.95, 50.83, 50.48, 50.24, 49.78, 50.0, 49.52, 50.19, 50.08, 50.16, 50.35, 50.38, 49.97, 50.38, 50.48, 49.92, 50.13, 50.19, 50.32, 50.38, 49.92, 50.43, 50.59, 50.4, 50.35, 50.05, 50.56, 50.43, 49.87, 49.97, 49.57, 49.6, 50.05, 50.22, 50.62, 50.08, 50.48, 49.62, 50.27, 49.49, 50.13, 49.84, 49.62, 49.65]
fed_sync_sgd_1 = [14.65, 15.11, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 16.16, 10.03, 10.62, 11.08, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.81, 10.83, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.91, 10.97, 10.97, 10.97, 10.91, 10.99, 10.99, 10.99, 10.91, 10.91, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.99, 10.97, 10.97, 10.97, 10.97, 10.97]
fed_sync_sgd_01 = [13.31, 11.53, 11.34, 12.1, 13.28, 13.98, 14.87, 15.32, 15.51, 16.21, 16.56, 16.72, 16.85, 17.23, 17.28, 17.39, 17.74, 17.9, 17.88, 17.85, 17.8, 17.74, 17.8, 17.85, 17.66, 17.77, 17.85, 17.85, 17.93, 17.98, 18.01, 17.96, 17.98, 17.96, 17.85, 17.74, 17.74, 17.63, 17.63, 17.63, 17.69, 17.69, 17.72, 17.69, 17.69, 17.69, 17.72, 17.69, 17.69, 17.72, 17.72, 17.72, 17.63, 17.55, 17.55, 17.58, 17.63, 17.72, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.74, 17.77, 17.77, 17.77, 17.77, 17.77]
fed_sync_sgd_001 = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.55, 2.61, 2.66, 2.69, 2.77, 2.93, 3.09, 3.31, 3.68, 3.79, 3.87, 3.9, 3.92, 3.92, 3.92, 3.92, 4.03, 4.03, 4.11, 4.11, 4.14, 4.11, 4.11, 4.14, 4.17, 4.22, 4.25, 4.3, 4.3, 4.3, 4.3, 4.3, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.33, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35, 4.35]
fed_sync_sgd_0001 = [5.0, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.0, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.08, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.13, 5.11, 5.11, 5.11, 5.05, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
