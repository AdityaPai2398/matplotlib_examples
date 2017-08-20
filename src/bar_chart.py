import matplotlib.pyplot as plt

incoming_email_at_hour = [8, 8, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 18]

hours = [x for x in range(6, 18)]

plt.hist(incoming_email_at_hour, hours, histtype='bar', rwidth=0.8)

plt.xlabel('t in hour')
plt.ylabel('incoming emails')

plt.title('Functions')
plt.legend()
plt.show()
