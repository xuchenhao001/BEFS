import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [59.62, 64.33, 66.26, 67.74, 69.01, 70.51, 72.63, 74.6, 76.05, 77.15, 78.33, 79.17, 79.62, 80.13, 80.46, 80.73, 80.91, 80.99, 81.08, 81.26, 81.26, 81.34, 81.75, 81.72, 81.72, 81.83, 82.04, 81.94, 82.04, 82.58, 82.8, 82.72, 82.69, 82.85, 82.9, 82.9, 83.04, 83.09, 83.06, 82.96, 83.41, 83.41, 83.63, 83.66, 83.68, 83.6, 83.49, 83.71, 83.92, 83.87, 83.84, 83.79, 83.84, 83.79, 83.9, 84.01, 83.84, 84.06, 84.01, 83.98, 84.19, 84.33, 84.06, 84.7, 84.57, 84.6, 84.3, 84.25, 84.3, 84.35, 84.57, 84.81, 84.38, 84.97, 84.95, 84.89, 84.73, 84.73, 84.81, 84.7, 84.52, 84.95, 85.05, 84.57, 84.54, 84.92, 84.62, 84.78, 84.87, 85.11, 85.03, 85.03, 85.0, 85.05, 84.81, 85.08, 85.11, 85.11, 84.87, 84.73, 84.92, 85.11, 84.95, 84.89, 85.11, 85.22, 85.16, 84.97, 85.0, 84.97, 85.05, 85.24, 85.13, 85.13, 85.0, 85.19, 85.35, 85.0, 85.27, 85.05, 85.13, 85.22, 85.27, 85.08, 84.97, 85.03, 85.0, 85.11, 85.08, 85.3, 85.19, 85.13, 85.19, 85.19, 85.35, 85.22, 84.97, 85.19, 85.08, 85.32, 85.32, 85.46, 85.16, 85.13, 85.11, 85.24, 85.46, 85.4, 85.3, 85.27, 85.22, 85.32, 85.62, 85.56, 85.51, 85.46, 85.4, 85.19, 85.4, 85.4, 85.46, 85.48, 85.51, 85.32, 85.03, 85.27, 85.43, 85.22, 85.43, 85.43, 85.54, 85.54, 85.32, 85.32, 85.62, 85.62, 85.56, 85.27, 85.59, 85.67, 85.4, 85.32, 85.59, 85.3, 85.35, 85.56, 85.3, 85.67, 85.56, 85.13, 85.48, 85.4, 85.62, 85.62, 85.32, 85.48, 85.43, 85.3, 85.78, 85.59]
fed_efsign = [59.78, 58.68, 60.11, 59.6, 59.68, 59.49, 60.03, 59.68, 60.46, 59.68, 60.86, 59.84, 60.97, 59.76, 60.65, 59.89, 60.65, 60.13, 60.62, 60.48, 61.1, 60.94, 61.26, 61.02, 61.56, 61.48, 61.94, 61.83, 62.39, 62.39, 62.72, 62.96, 63.31, 63.66, 63.79, 64.46, 64.78, 65.67, 65.81, 66.37, 67.18, 67.04, 67.74, 67.88, 68.44, 68.39, 68.9, 68.71, 69.3, 69.11, 70.0, 69.68, 70.11, 69.62, 70.19, 69.87, 70.05, 69.84, 70.03, 70.38, 70.56, 70.59, 70.78, 70.99, 71.34, 70.67, 71.61, 70.86, 71.91, 71.05, 72.18, 71.02, 72.77, 71.77, 72.93, 71.83, 72.72, 71.69, 73.49, 72.12, 73.44, 72.1, 73.84, 72.63, 73.92, 72.9, 74.03, 72.45, 74.03, 72.58, 74.35, 71.99, 73.87, 72.2, 72.58, 71.37, 73.41, 71.37, 72.9, 71.69, 73.23, 71.99, 73.25, 72.69, 73.23, 72.34, 73.17, 71.69, 73.09, 72.5, 73.2, 72.53, 73.82, 73.15, 73.84, 72.88, 74.01, 72.85, 73.79, 73.09, 74.09, 72.47, 74.41, 72.74, 73.84, 73.36, 74.3, 73.09, 73.9, 73.04, 74.06, 73.23, 74.01, 72.9, 74.68, 73.09, 74.14, 72.93, 74.19, 73.12, 74.44, 73.28, 74.87, 73.49, 73.98, 72.98, 74.49, 72.82, 74.11, 72.98, 73.84, 73.31, 74.25, 73.39, 73.76, 73.2, 73.92, 74.09, 73.31, 73.47, 73.79, 73.33, 73.04, 73.79, 73.76, 73.95, 73.98, 74.25, 74.25, 66.94, 74.38, 73.84, 75.03, 74.54, 75.91, 74.73, 75.75, 74.89, 75.59, 74.14, 75.35, 73.68, 75.22, 73.84, 75.24, 74.06, 75.38, 74.11, 74.97, 73.87, 74.92, 74.52, 75.4, 74.81, 75.86, 74.62, 75.94, 74.14, 75.65, 74.65]
fed_sync = [46.88, 55.11, 62.28, 64.65, 66.08, 71.32, 72.98, 73.68, 74.38, 74.95, 76.05, 75.91, 76.34, 76.94, 77.02, 77.42, 77.72, 77.8, 78.49, 78.39, 78.76, 78.76, 78.98, 79.14, 79.44, 79.35, 79.68, 79.52, 79.81, 79.84, 80.0, 80.11, 80.19, 80.43, 80.43, 80.54, 80.48, 80.56, 80.62, 81.08, 81.13, 81.05, 80.97, 80.99, 81.18, 81.16, 81.29, 81.24, 81.56, 81.34, 81.61, 81.64, 81.42, 81.34, 81.42, 81.64, 81.59, 81.77, 81.85, 82.02, 81.99, 81.83, 81.96, 82.07, 82.23, 82.18, 81.91, 81.96, 82.07, 82.12, 82.2, 82.55, 82.15, 81.88, 82.5, 82.2, 82.47, 82.37, 82.28, 82.31, 82.28, 82.61, 82.85, 82.63, 82.47, 82.37, 82.85, 82.47, 82.69, 82.5, 82.66, 82.61, 82.98, 82.82, 82.45, 82.88, 82.55, 82.8, 82.85, 82.66, 82.8, 82.82, 82.8, 82.93, 83.09, 82.82, 82.72, 82.82, 82.69, 82.88, 82.82, 83.01, 83.01, 83.06, 83.12, 82.96, 83.23, 82.96, 83.23, 83.25, 83.06, 82.8, 83.09, 83.17, 83.31, 83.25, 83.28, 83.15, 83.31, 83.2, 83.28, 83.06, 83.31, 82.96, 83.23, 82.96, 82.98, 83.33, 83.06, 82.88, 83.12, 83.12, 83.28, 83.2, 83.23, 83.01, 83.41, 83.47, 83.17, 83.41, 83.36, 83.15, 83.39, 83.63, 83.25, 83.2, 83.23, 83.06, 83.31, 83.47, 83.36, 83.39, 83.2, 83.28, 83.28, 83.36, 83.44, 83.49, 83.58, 83.28, 83.58, 83.58, 83.36, 83.41, 83.36, 83.68, 83.58, 83.39, 83.33, 83.31, 83.23, 83.39, 83.76, 83.36, 83.52, 83.41, 83.87, 83.52, 83.41, 83.52, 83.39, 83.44, 83.2, 83.6, 83.52, 83.55, 83.33, 83.41, 83.28, 83.41]
fed_sync_sgd = [50.46, 50.24, 51.16, 52.04, 51.88, 54.62, 53.63, 56.29, 55.62, 57.18, 57.58, 57.53, 59.22, 58.15, 59.78, 58.6, 60.38, 58.9, 60.65, 59.38, 61.24, 59.87, 61.72, 59.97, 62.02, 60.16, 62.07, 60.24, 62.2, 60.73, 62.37, 61.02, 62.72, 61.32, 62.69, 61.42, 63.04, 61.8, 63.23, 61.99, 63.28, 62.02, 63.49, 62.18, 63.66, 62.28, 63.76, 62.34, 63.9, 62.55, 64.19, 62.93, 64.44, 63.17, 64.6, 63.58, 64.84, 63.84, 64.89, 63.87, 64.81, 64.01, 64.95, 64.3, 65.0, 64.38, 65.08, 64.46, 65.08, 64.6, 65.19, 64.78, 65.16, 64.81, 65.22, 64.76, 65.35, 64.92, 65.35, 64.97, 65.51, 65.43, 65.78, 65.51, 65.73, 65.62, 65.65, 65.62, 65.54, 65.78, 65.43, 65.83, 65.4, 66.08, 65.65, 65.97, 65.62, 66.08, 65.46, 65.4, 65.43, 65.43, 65.48, 65.38, 65.46, 65.48, 65.48, 65.54, 65.59, 65.56, 65.62, 65.62, 65.7, 65.73, 65.78, 65.81, 65.81, 65.89, 65.89, 65.83, 65.83, 65.86, 65.83, 65.83, 65.89, 65.89, 65.94, 65.97, 66.05, 65.99, 65.99, 66.08, 66.1, 66.13, 66.13, 66.1, 66.13, 66.13, 66.1, 66.1, 66.1, 66.1, 66.1, 66.21, 66.24, 66.21, 66.18, 66.13, 66.18, 66.18, 66.21, 66.21, 66.16, 66.16, 66.16, 66.16, 66.18, 66.18, 66.18, 66.18, 66.16, 66.16, 66.13, 66.13, 66.13, 66.16, 66.16, 66.18, 66.21, 66.21, 66.24, 66.24, 66.24, 66.24, 66.26, 66.26, 66.24, 66.24, 66.24, 66.21, 66.26, 66.29, 66.29, 66.32, 66.32, 66.34, 66.37, 66.37, 66.4, 66.4, 66.4, 66.4, 66.42, 66.37, 66.37, 66.37, 66.37, 66.37, 66.37, 66.37]
local_train = [80.48, 85.7, 86.91, 87.2, 88.15, 87.98, 88.33, 88.23, 88.44, 88.31, 88.55, 88.63, 88.44, 88.95, 88.82, 88.87, 88.95, 88.82, 88.76, 88.79, 88.95, 89.14, 88.98, 88.9, 89.01, 89.17, 89.65, 89.62, 89.76, 89.73, 89.95, 90.19, 90.22, 90.22, 90.22, 90.3, 90.46, 90.43, 90.38, 90.35, 90.67, 91.1, 90.99, 91.24, 91.05, 91.13, 91.13, 91.13, 91.42, 91.26, 91.21, 91.24, 90.99, 90.75, 91.32, 91.21, 91.26, 91.18, 91.61, 91.24, 91.48, 91.53, 91.51, 91.45, 91.56, 91.48, 91.48, 91.42, 91.42, 91.26, 91.61, 91.45, 91.08, 91.45, 91.21, 91.32, 91.42, 91.37, 91.26, 91.32, 91.32, 91.59, 91.48, 91.53, 91.4, 91.59, 91.48, 91.45, 91.45, 91.45, 91.13, 91.24, 91.48, 91.53, 91.53, 91.64, 91.45, 91.53, 91.26, 91.34, 91.42, 91.34, 91.64, 91.45, 91.56, 91.51, 91.69, 91.69, 91.69, 91.53, 91.45, 91.24, 91.67, 91.48, 91.61, 91.51, 91.45, 91.53, 91.61, 91.53, 91.18, 91.42, 91.42, 91.67, 91.64, 91.34, 91.61, 91.56, 91.45, 91.64, 91.59, 91.29, 91.59, 91.16, 91.32, 91.32, 91.45, 91.53, 91.4, 91.45, 91.45, 91.67, 91.59, 91.67, 91.48, 91.42, 91.75, 91.51, 91.4, 91.51, 91.45, 91.34, 91.45, 91.61, 91.48, 91.42, 91.59, 91.37, 91.42, 91.37, 91.59, 91.51, 91.56, 91.53, 91.34, 91.26, 91.42, 91.42, 91.4, 91.56, 91.64, 91.32, 91.48, 91.53, 91.34, 91.45, 91.29, 91.32, 91.67, 91.69, 91.37, 91.8, 91.42, 91.24, 91.45, 91.53, 91.59, 91.34, 91.45, 91.37, 91.51, 91.56, 91.53, 91.51, 91.45, 91.37, 91.29, 91.45, 91.34, 91.34]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_efsign, fed_avg, local_train, save_path, plot_size="M")