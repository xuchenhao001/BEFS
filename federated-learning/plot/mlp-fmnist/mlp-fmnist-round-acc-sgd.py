import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [48.15, 61.45, 64.65, 67.58, 69.57, 70.94, 71.8, 72.23, 72.88, 73.25, 73.74, 74.09, 74.44, 74.97, 75.16, 75.56, 75.67, 76.77, 77.12, 77.69, 78.04, 78.17, 78.74, 78.9, 79.54, 79.62, 79.78, 79.78, 80.65, 80.43, 80.43, 80.46, 80.48, 80.83, 80.83, 81.29, 81.45, 81.61, 81.53, 81.8, 82.1, 82.18, 82.1, 82.66, 82.74, 82.37, 83.12, 82.72, 83.01, 83.04, 82.96, 82.72, 82.63, 83.15, 82.98, 83.2, 83.06, 83.28, 83.28, 83.25, 83.49, 83.47, 83.49, 83.82, 83.79, 83.31, 83.55, 83.55, 83.87, 84.03, 83.95, 83.63, 84.09, 83.92, 83.79, 84.46, 84.14, 84.09, 84.44, 83.92, 83.68, 83.79, 84.03, 84.14, 83.79, 83.41, 83.76, 84.14, 84.09, 84.35, 84.68, 84.17, 84.44, 84.33, 84.27, 84.33, 83.92, 84.41, 84.7, 84.33, 83.71, 84.17, 84.57, 84.35, 84.49, 84.25, 84.52, 84.44, 84.19, 84.65, 84.65, 84.87, 84.19, 84.41, 84.7, 84.95, 84.87, 84.78, 84.35, 84.57, 84.87, 84.6, 84.52, 84.3, 84.57, 84.84, 84.97, 84.95, 85.03, 84.92, 84.7, 84.65, 84.81, 84.7, 84.73, 84.81, 84.84, 84.89, 84.76, 84.49, 84.49, 84.89, 84.97, 85.19, 84.84, 85.24, 85.13, 84.76, 84.81, 84.89, 84.87, 84.97, 84.84, 84.52, 84.73, 85.03, 85.22, 84.57, 84.89, 84.57, 85.05, 85.08, 84.87, 84.95, 84.78, 85.0, 85.16, 85.32, 85.0, 84.65, 84.65, 84.92, 84.84, 84.81, 84.92, 85.13, 84.65, 84.6, 85.03, 85.19, 84.76, 84.92, 84.95, 84.87, 85.13, 85.08, 85.22, 84.84, 84.76, 84.97, 84.68, 85.19, 84.92, 84.76, 85.13, 84.84, 84.52, 85.19, 84.65, 84.92]
fed_sync = [42.28, 50.16, 57.07, 60.75, 65.35, 67.74, 68.74, 69.89, 70.54, 71.08, 72.28, 73.74, 73.47, 74.03, 74.95, 74.7, 75.62, 75.56, 75.91, 76.85, 76.75, 77.1, 77.45, 77.23, 77.42, 77.45, 77.96, 77.8, 77.98, 77.85, 78.25, 78.25, 78.23, 78.28, 78.44, 78.39, 78.44, 79.09, 78.92, 78.98, 79.41, 79.01, 78.92, 79.11, 78.95, 79.3, 79.41, 79.27, 79.3, 78.9, 79.38, 79.25, 79.62, 79.25, 79.41, 79.76, 79.49, 79.35, 79.76, 79.54, 79.62, 79.84, 80.0, 79.76, 79.95, 80.03, 79.76, 79.84, 79.92, 80.03, 80.08, 80.08, 79.95, 79.78, 80.3, 80.24, 80.38, 80.19, 80.48, 80.78, 81.02, 80.7, 80.43, 80.65, 80.54, 80.75, 80.7, 80.59, 80.48, 80.7, 80.91, 80.83, 81.08, 80.73, 80.91, 80.43, 80.89, 80.67, 81.05, 80.97, 80.65, 80.86, 80.94, 80.99, 81.1, 81.05, 81.21, 81.1, 80.99, 80.99, 81.1, 80.75, 81.16, 80.94, 80.91, 80.86, 81.18, 81.08, 81.02, 81.02, 81.1, 80.94, 80.91, 81.13, 81.1, 81.08, 80.91, 80.89, 81.08, 80.99, 81.18, 81.1, 80.7, 81.05, 81.1, 81.1, 81.21, 81.16, 80.94, 81.24, 81.05, 81.37, 81.18, 81.08, 80.94, 81.1, 80.91, 81.13, 81.26, 80.86, 81.37, 81.02, 80.94, 80.83, 81.05, 81.05, 81.16, 81.18, 81.02, 81.24, 81.08, 81.24, 81.08, 81.13, 80.97, 81.21, 81.13, 81.26, 81.24, 81.24, 81.21, 81.48, 81.45, 81.37, 81.1, 81.34, 81.4, 80.94, 81.26, 81.26, 81.4, 81.26, 81.1, 81.24, 81.29, 81.26, 81.16, 81.37, 81.21, 81.32, 81.32, 81.18, 81.24, 81.21, 81.42, 81.45, 81.13, 81.34, 81.29, 81.4]
fed_sync_sgd_1 = [36.29, 6.56, 41.42, 6.64, 55.19, 7.39, 54.22, 16.1, 50.99, 11.24, 47.45, 11.59, 48.55, 20.86, 46.02, 22.04, 46.69, 23.33, 52.39, 28.39, 56.1, 23.71, 51.77, 25.48, 56.13, 25.32, 55.32, 23.33, 56.64, 23.76, 53.17, 26.72, 55.13, 23.55, 58.76, 24.81, 58.25, 25.19, 54.33, 30.24, 58.52, 28.71, 55.05, 27.55, 57.1, 24.01, 52.5, 25.13, 53.41, 30.27, 53.6, 31.8, 56.4, 26.02, 59.81, 21.26, 60.56, 26.53, 58.44, 31.8, 59.84, 33.55, 56.53, 25.89, 59.06, 27.88, 60.35, 33.31, 59.25, 27.12, 57.5, 26.83, 55.65, 27.34, 56.05, 31.16, 56.53, 31.29, 56.64, 26.29, 56.02, 24.46, 56.48, 29.44, 57.18, 26.34, 62.18, 25.4, 62.96, 25.94, 62.15, 29.06, 62.72, 31.18, 64.89, 29.89, 63.33, 29.97, 63.12, 61.85, 62.74, 63.66, 63.68, 64.73, 64.22, 64.92, 65.05, 65.67, 66.13, 66.48, 67.1, 67.47, 67.58, 67.93, 67.58, 67.63, 66.94, 67.5, 65.99, 66.42, 64.87, 65.54, 64.19, 64.89, 63.15, 64.03, 62.42, 63.79, 61.61, 62.96, 60.91, 62.45, 60.38, 61.88, 60.05, 61.96, 59.62, 61.69, 59.11, 61.42, 59.52, 61.32, 59.84, 62.18, 59.97, 61.72, 59.52, 61.29, 59.19, 61.02, 58.79, 60.81, 58.92, 60.81, 58.98, 60.86, 59.11, 61.67, 59.7, 61.64, 59.41, 61.67, 59.57, 62.04, 60.46, 62.66, 60.75, 62.74, 60.56, 62.45, 60.27, 62.12, 59.84, 61.75, 59.87, 61.85, 59.92, 61.85, 59.73, 61.8, 59.35, 61.24, 59.06, 60.78, 58.92, 60.62, 58.9, 60.62, 59.49, 61.21, 59.38, 61.26, 59.46, 61.45, 59.62, 61.45, 59.44, 61.32, 59.14, 59.38]
fed_sync_sgd_01 = [53.58, 51.42, 53.33, 52.69, 54.17, 53.95, 55.38, 55.65, 56.83, 57.12, 57.42, 57.85, 57.98, 58.15, 58.44, 58.66, 58.82, 59.17, 59.19, 59.44, 59.41, 60.43, 59.65, 61.26, 59.81, 61.88, 59.87, 62.53, 59.84, 62.9, 59.81, 63.33, 60.03, 63.44, 60.19, 63.23, 60.22, 63.55, 60.24, 63.98, 60.24, 64.44, 60.3, 64.57, 60.38, 64.38, 60.67, 63.76, 60.65, 63.2, 60.89, 62.9, 61.26, 63.06, 61.24, 63.36, 61.34, 63.92, 61.34, 64.11, 61.48, 64.54, 61.64, 65.24, 61.75, 65.83, 62.02, 66.18, 62.42, 66.18, 63.06, 66.53, 63.58, 66.77, 63.9, 66.8, 64.11, 67.1, 64.46, 67.28, 64.89, 67.39, 64.97, 67.47, 65.13, 67.5, 65.13, 67.55, 65.24, 67.66, 65.35, 67.82, 65.59, 68.01, 65.83, 68.12, 65.83, 68.12, 65.89, 66.02, 65.83, 65.99, 65.89, 65.94, 65.86, 65.89, 65.89, 65.97, 65.75, 65.86, 65.65, 65.81, 65.7, 65.89, 65.78, 65.89, 65.73, 65.83, 65.73, 65.73, 65.67, 65.73, 65.7, 65.75, 65.67, 65.78, 65.73, 65.75, 65.73, 65.75, 65.73, 65.78, 65.73, 65.83, 65.86, 65.86, 65.86, 65.78, 65.78, 65.75, 65.75, 65.86, 65.81, 65.81, 65.75, 65.78, 65.73, 65.75, 65.67, 65.75, 65.67, 65.67, 65.67, 65.65, 65.65, 65.65, 65.65, 65.73, 65.78, 65.78, 65.7, 65.78, 65.78, 65.75, 65.73, 65.73, 65.7, 65.73, 65.56, 65.59, 65.67, 65.78, 65.78, 65.81, 65.78, 65.86, 65.78, 65.86, 65.83, 65.86, 65.83, 65.81, 65.75, 65.73, 65.62, 65.73, 65.73, 65.78, 65.83, 65.89, 65.89, 65.99, 65.97, 66.02, 65.99, 66.02, 66.02, 65.99, 65.97, 65.94]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd_1, fed_sync_sgd_01, fed_sync, fed_avg, save_path, plot_size="L")
