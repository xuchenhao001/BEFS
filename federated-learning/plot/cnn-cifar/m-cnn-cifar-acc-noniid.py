import sys

from plot.utils.time_acc_base import plot_time_acc

fed_sync_sgd = [18.82, 23.31, 24.27, 28.82, 30.32, 32.93, 33.2, 35.91, 36.05, 39.03, 38.71, 41.05, 40.3, 41.08, 41.29, 42.04, 42.1, 42.5, 42.85, 43.04, 42.85, 43.31, 43.41, 44.3, 44.03, 44.92, 43.87, 44.65, 44.17, 45.03, 44.52, 45.56, 44.73, 45.99, 44.87, 46.02, 45.3, 46.53, 45.7, 46.72, 46.61, 46.99, 47.12, 47.69, 46.94, 47.72, 47.04, 47.74, 47.34, 47.61, 47.07, 47.85, 47.37, 48.41, 47.9, 48.66, 48.17, 48.17, 48.15, 48.33, 48.23, 48.58, 48.47, 48.84, 48.71, 49.49, 48.95, 48.98, 48.36, 48.58, 48.66, 49.06, 48.87, 49.06, 48.58, 48.98, 48.55, 48.95, 48.63, 48.95, 48.55, 49.44, 49.19, 49.3, 48.87, 48.79, 48.71, 48.52, 48.01, 48.47, 48.76, 48.47, 48.17, 48.74, 48.17, 48.71, 48.12, 48.87, 48.23, 49.06, 48.41, 48.92, 48.25, 48.58, 48.28, 48.95, 48.23, 48.58, 48.15, 49.17, 48.44, 49.7, 48.95, 49.09, 48.71, 49.03, 48.39, 48.76, 48.36, 49.09, 48.06, 48.63, 48.52, 49.25, 49.3, 49.22, 49.01, 49.41, 49.27, 49.65, 48.95, 49.14, 48.58, 48.52, 48.63, 48.92, 48.25, 48.95, 48.6, 49.14, 48.74, 48.41, 48.79, 48.71, 48.6, 48.74, 47.8, 48.55, 48.52, 48.76, 48.44, 49.01, 47.98, 48.41, 47.85, 48.39, 48.41, 48.55, 48.49, 48.66, 48.15, 48.17, 47.74, 47.88, 48.31, 47.93, 48.44, 48.52, 48.79, 48.6, 48.31, 48.17, 48.04, 48.68, 47.74, 48.01, 48.12, 48.44, 48.39, 48.41, 47.96, 48.23, 48.12, 47.9, 48.17, 48.33, 48.01, 48.06, 47.31, 47.69, 47.8, 48.2, 48.23, 48.55, 48.31, 48.31, 47.5, 48.28, 48.04, 48.68]
fed_avg = [22.39, 30.4, 35.13, 39.65, 43.33, 45.83, 47.72, 49.14, 49.97, 49.95, 50.97, 50.19, 50.75, 51.16, 51.24, 51.77, 51.48, 51.64, 51.85, 51.53, 51.42, 51.56, 51.64, 51.88, 51.83, 51.77, 51.88, 51.51, 51.85, 51.64, 50.86, 51.08, 50.89, 50.78, 51.34, 51.29, 51.16, 50.89, 50.48, 50.67, 50.73, 50.62, 50.3, 50.62, 49.84, 49.97, 49.7, 50.24, 49.65, 49.81, 50.19, 50.43, 50.27, 50.4, 50.19, 50.56, 50.19, 50.24, 49.68, 50.62, 50.32, 50.62, 50.54, 50.48, 50.73, 50.46, 50.4, 50.51, 49.97, 50.7, 49.84, 50.22, 50.05, 49.89, 50.51, 49.73, 50.13, 49.57, 49.87, 50.46, 49.78, 49.89, 49.92, 50.22, 50.35, 50.03, 50.81, 50.75, 50.13, 50.54, 50.48, 50.75, 50.27, 49.92, 50.43, 50.08, 50.89, 50.78, 50.43, 50.7, 50.22, 50.83, 50.62, 50.22, 50.19, 50.13, 50.91, 50.48, 50.78, 50.94, 50.38, 50.94, 51.02, 50.59, 50.75, 50.43, 50.62, 50.54, 50.86, 51.08, 50.24, 51.08, 50.7, 50.43, 50.83, 50.54, 49.78, 49.78, 50.27, 50.35, 50.48, 50.67, 50.4, 50.48, 50.51, 50.75, 50.62, 51.21, 50.67, 50.48, 50.59, 50.7, 50.67, 50.43, 50.46, 50.54, 50.75, 50.67, 50.32, 50.48, 50.38, 50.54, 50.7, 50.35, 50.56, 50.35, 49.78, 50.4, 50.46, 50.38, 51.1, 50.59, 50.81, 50.56, 50.35, 49.95, 50.27, 50.43, 50.46, 50.35, 50.24, 50.46, 50.16, 50.67, 50.43, 50.56, 50.7, 50.62, 50.43, 50.67, 50.54, 50.05, 50.83, 50.54, 50.54, 50.86, 50.59, 50.75, 50.43, 50.38, 50.78, 50.7, 50.27, 50.51, 50.24, 50.32, 50.38, 50.4, 50.54, 50.32]
fed_efsign = [10.0, 18.12, 33.9, 34.01, 34.35, 34.54, 35.38, 35.24, 34.76, 35.97, 34.84, 37.96, 36.18, 38.68, 37.55, 39.44, 37.85, 39.3, 38.41, 39.38, 39.01, 40.08, 38.92, 39.49, 39.84, 39.68, 39.97, 39.97, 40.22, 39.49, 39.6, 40.0, 40.65, 40.38, 40.54, 40.51, 40.86, 40.35, 40.94, 39.41, 40.13, 41.1, 40.67, 39.7, 41.1, 38.82, 40.83, 38.06, 40.73, 39.7, 39.68, 41.05, 41.48, 39.89, 40.99, 40.27, 40.32, 40.59, 40.7, 39.97, 41.05, 41.13, 40.13, 41.16, 41.88, 40.43, 40.03, 39.57, 39.62, 40.13, 41.77, 40.99, 41.64, 40.89, 39.84, 40.08, 40.7, 40.13, 40.46, 40.4, 40.54, 40.75, 41.42, 39.78, 40.43, 40.62, 38.52, 38.33, 40.38, 40.24, 40.46, 39.62, 37.02, 41.37, 39.25, 39.6, 39.87, 40.22, 39.78, 39.3, 39.54, 40.54, 39.22, 40.97, 36.69, 40.08, 38.71, 39.95, 40.97, 38.58, 39.27, 42.04, 39.65, 39.33, 37.9, 40.32, 39.81, 40.11, 40.05, 38.68, 39.03, 40.86, 41.91, 40.81, 41.24, 39.95, 33.01, 41.16, 40.22, 40.7, 39.54, 36.85, 41.88, 41.34, 39.78, 40.62, 39.44, 40.62, 41.37, 42.04, 39.87, 39.6, 40.43, 40.3, 40.08, 40.19, 39.44, 40.0, 39.41, 40.91, 39.89, 40.38, 37.72, 40.7, 37.98, 40.05, 37.98, 40.32, 39.46, 41.08, 38.63, 39.35, 39.22, 40.19, 37.8, 38.92, 38.06, 40.75, 37.37, 38.82, 36.53, 39.25, 36.61, 40.43, 39.68, 37.15, 39.44, 37.77, 39.84, 34.87, 36.42, 34.09, 39.17, 40.13, 37.93, 35.75, 37.15, 34.84, 39.57, 39.14, 37.47, 37.39, 39.78, 38.01, 39.81, 39.25, 38.76, 38.63, 39.87, 39.19]
local_train = [50.97, 61.02, 65.24, 65.7, 65.86, 66.29, 66.99, 66.94, 66.99, 67.26, 67.18, 67.1, 66.99, 67.1, 67.02, 67.04, 66.99, 66.91, 67.02, 66.94, 66.96, 66.99, 66.99, 67.02, 67.04, 67.02, 67.1, 67.1, 67.04, 67.07, 67.18, 67.18, 67.12, 67.12, 67.1, 67.04, 67.04, 67.02, 66.99, 66.96, 66.96, 66.96, 66.94, 66.94, 66.96, 66.96, 66.94, 66.96, 67.02, 66.96, 66.96, 66.94, 66.96, 66.94, 66.91, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.94, 66.91, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.99, 66.96, 66.99, 66.94, 66.94, 66.96, 66.96, 66.96, 66.99, 66.96, 66.96, 66.96, 66.96, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.96, 66.91, 66.91, 66.91, 66.91, 66.88, 66.88, 66.88, 66.88, 66.88, 66.91, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.88, 66.91, 66.91, 66.91, 66.91, 66.91, 66.91, 66.91, 66.94, 66.91, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.94, 66.96, 66.94, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.99, 66.96, 66.96, 66.99, 66.96, 66.99, 66.96, 66.96, 66.96, 66.96]
fed_sign = [26.26, 22.5, 23.84, 24.65, 25.67, 25.97, 24.92, 25.27, 25.05, 25.97, 26.34, 27.53, 29.57, 28.63, 28.52, 27.93, 29.87, 31.37, 30.67, 31.24, 32.02, 32.26, 33.25, 32.88, 34.11, 33.92, 33.79, 33.92, 35.05, 34.44, 35.35, 35.62, 33.79, 35.62, 36.91, 36.56, 36.75, 35.11, 36.16, 36.67, 36.29, 37.82, 38.6, 37.77, 38.09, 35.83, 36.61, 38.04, 37.15, 38.84, 37.93, 34.95, 35.73, 39.19, 38.39, 37.74, 38.25, 36.53, 37.18, 39.19, 39.49, 36.94, 37.53, 39.27, 38.28, 37.5, 38.15, 37.66, 36.75, 39.54, 39.65, 36.53, 38.25, 38.92, 37.1, 36.34, 36.83, 38.36, 37.53, 37.39, 39.09, 36.61, 37.98, 37.2, 36.24, 35.97, 38.49, 39.49, 37.23, 38.31, 38.9, 37.1, 38.39, 38.82, 38.55, 38.04, 38.92, 38.9, 36.02, 36.32, 37.45, 37.9, 38.33, 38.71, 38.79, 38.63, 38.6, 38.23, 38.12, 38.41, 38.68, 38.52, 38.76, 38.44, 38.52, 38.66, 38.47, 38.74, 38.87, 38.98, 39.27, 38.92, 38.71, 38.36, 37.98, 38.06, 38.09, 37.9, 38.41, 38.33, 38.31, 38.28, 38.47, 38.41, 38.58, 38.92, 39.11, 38.82, 38.66, 39.11, 38.79, 38.82, 39.06, 38.95, 38.76, 38.9, 38.66, 38.68, 38.87, 38.87, 38.9, 38.84, 38.87, 38.9, 38.92, 38.92, 38.92, 38.92, 38.9, 38.9, 38.82, 38.76, 38.74, 38.66, 38.63, 38.68, 38.66, 38.76, 38.82, 38.74, 38.79, 38.76, 38.74, 38.63, 38.66, 38.66, 38.68, 38.71, 38.84, 38.9, 38.92, 38.87, 38.92, 38.82, 38.95, 38.9, 38.98, 38.92, 38.84, 38.9, 38.84, 38.9, 38.92, 38.98, 38.95, 38.92, 38.95, 39.06, 39.14, 39.09]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_efsign, fed_sign, fed_avg, local_train, save_path, plot_size="3")
