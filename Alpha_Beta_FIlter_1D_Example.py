"""
Module: Alpha Beta Filter 1D
Desc: This module is an alpha beta filter for a car moving at a constant velocity 
"""
import random
import matplotlib.pyplot as plt

TIME_STEPS = 10
DT = 1
VELOCITY = 5
ALPHA = 0.6
BETA = 0.6


def Alpha_Beta_filter(alpha, beta, measured_pos):
    filtered_pos = [0]
    filtered_vel = [5]
    for i in range(1, len(measured_pos)):
        # predict equations for constant velocity
        predict_pos = filtered_pos[i-1] + DT * filtered_vel[i-1]
        predict_velocity = filtered_vel[i-1]

        # state update
        new_pos = predict_pos + alpha * (measured_pos[i] - predict_pos)
        new_vel = predict_velocity + beta * \
            (measured_pos[i] - predict_pos) / DT

        filtered_pos.append(new_pos)
        filtered_vel.append(new_vel)

    return filtered_pos


def real_vehical_motion(t_total, real_velocity, dt):
    # Calaculate the real position of the vehical
    real_position = [0]
    for i in range(t_total):
        random_slip_factor = random.uniform(0.7, 1)
        if i > 0:
            new_position = real_position[i - 1] + \
                real_velocity * dt * random_slip_factor
            round_pos = round(new_position, 2)
            real_position.append(round_pos)

    # Create time axis for plot
    time_axis = []
    for i in range(t_total):
        point_in_time = i * dt
        time_axis.append(point_in_time)

    return real_position, time_axis


def noisy_measure(real_pos):
    noisy_pos = [0]
    for val in real_pos[1:]:  # start from second element
        noise = round(random.uniform(-4, 4), 2)
        noisy_pos.append(val + noise)
    return noisy_pos


def plot_data(x, real, noise, filtered):
    plt.plot(x, real, label="Real position")
    plt.plot(x, noise, label="Noisy position")
    plt.plot(x, filtered, label="Filtered position")
    plt.grid(True)
    plt.legend()

    plt.show()


real_pos, time_axis = real_vehical_motion(TIME_STEPS, VELOCITY, DT)
measured_pos = noisy_measure(real_pos)
filtered_pos = Alpha_Beta_filter(ALPHA, BETA, measured_pos)

print(len(filtered_pos))
print(real_pos)
plot_data(time_axis, real_pos, measured_pos, filtered_pos)
