import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [47.69, 54.3, 59.6, 64.14, 66.56, 68.12, 68.82, 70.75, 72.1, 71.96, 72.93, 74.06, 74.62, 75.35, 75.86, 75.62, 75.67, 76.8, 76.72, 76.96, 77.04, 77.23, 77.42, 77.98, 78.41, 78.66, 78.17, 78.17, 78.66, 78.87, 78.84, 78.79, 79.22, 79.65, 79.52, 79.46, 79.92, 79.25, 79.41, 79.87, 80.11, 79.95, 79.57, 79.87, 79.84, 80.43, 80.22, 80.35, 80.65, 80.3, 80.78, 80.75, 80.51, 81.02, 80.78, 81.26, 80.7, 80.67, 81.37, 80.78, 81.34, 81.59, 81.4, 81.02, 81.77, 81.51, 81.24, 81.61, 81.64, 81.56, 81.56, 80.99, 81.64, 81.85, 81.4, 80.94, 81.16, 81.85, 81.59, 81.77]
fed_sync = [53.49, 57.85, 59.25, 60.51, 62.15, 64.27, 66.64, 67.58, 68.74, 70.32, 71.53, 72.53, 72.66, 73.58, 73.66, 74.22, 74.46, 75.03, 75.32, 75.73, 75.91, 76.51, 76.59, 76.24, 76.61, 76.91, 78.09, 77.53, 77.23, 77.15, 77.98, 77.77, 77.66, 78.66, 78.15, 78.49, 78.41, 78.36, 78.66, 78.39, 79.06, 78.95, 79.14, 78.71, 78.55, 79.14, 79.46, 79.3, 78.68, 79.84, 79.27, 79.17, 79.33, 79.33, 79.52, 79.6, 79.54, 79.49, 78.6, 78.9, 80.22, 79.95, 80.0, 79.7, 79.25, 79.81, 79.35, 79.54, 79.78, 79.76, 80.32, 80.48, 79.95, 80.38, 80.22, 80.43, 79.78, 80.3, 80.0, 80.7]
fed_sync_sgd_1 = [47.1, 58.58, 63.6, 68.12, 61.05, 68.01, 68.68, 65.24, 72.74, 62.58, 74.14, 70.75, 70.19, 71.51, 75.08, 74.52, 77.93, 76.99, 75.65, 77.77, 79.01, 80.54, 80.97, 81.32, 81.42, 81.67, 81.64, 81.64, 81.83, 81.8, 81.8, 81.96, 82.02, 82.15, 82.07, 82.2, 81.99, 81.85, 82.15, 82.2, 82.18, 82.2, 82.23, 82.23, 82.23, 82.2, 82.26, 82.2, 82.15, 82.18, 82.2, 82.23, 82.23, 82.2, 82.2, 82.28, 82.18, 82.18, 82.2, 82.2, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.23, 82.2, 82.2, 82.2, 82.2, 82.2, 82.2]
fed_sync_sgd_01 = [59.49, 60.94, 65.03, 66.94, 68.87, 71.29, 71.72, 75.59, 74.87, 79.57, 74.81, 78.79, 75.78, 80.16, 76.64, 80.08, 76.24, 79.6, 77.15, 79.17, 80.81, 82.37, 82.85, 82.8, 82.69, 82.58, 83.01, 83.06, 82.66, 82.77, 82.72, 82.8, 82.85, 82.85, 82.69, 82.82, 82.85, 83.04, 82.98, 82.98, 83.04, 83.01, 83.04, 83.06, 83.09, 83.09, 83.09, 83.06, 83.01, 83.01, 83.01, 83.01, 83.04, 83.09, 83.06, 83.09, 83.12, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.04, 83.01, 83.01, 83.01, 83.01, 83.01, 83.01, 83.01, 83.01, 83.01]
fed_sync_sgd_001 = [22.28, 38.41, 41.83, 44.87, 47.69, 53.98, 57.77, 59.57, 60.19, 60.54, 60.97, 61.56, 62.26, 62.96, 63.63, 63.92, 64.09, 64.41, 64.7, 64.87, 64.95, 65.0, 65.03, 65.03, 65.03, 65.03, 65.05, 65.11, 65.13, 65.24, 65.35, 65.38, 65.4, 65.48, 65.54, 65.56, 65.62, 65.65, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.75, 65.86, 65.86, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89, 65.89]
fed_sync_sgd_0001 = [11.48, 12.74, 13.92, 16.08, 17.82, 19.19, 21.1, 23.44, 26.02, 29.06, 33.04, 36.99, 40.22, 44.57, 46.72, 49.33, 51.32, 52.8, 53.82, 53.9, 54.01, 54.09, 54.17, 54.3, 54.3, 54.41, 54.6, 54.68, 54.87, 54.92, 55.08, 55.11, 55.13, 55.24, 55.27, 55.32, 55.43, 55.46, 55.59, 55.62, 55.62, 55.62, 55.62, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.65, 55.67, 55.67, 55.67, 55.67, 55.67]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync_sgd_001, fed_sync_sgd_0001, fed_sync, fed_avg, save_path, plot_size="L")
