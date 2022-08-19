import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0,4])
ax.set_ylim([0,4])
ax.arrow(0,0,3,2.5,length_includes_head = True,
             head_length = 0.1,head_width = 0.05,color = 'r')
ax.arrow(0,0,1,2,length_includes_head = True,
             head_length = 0.1,head_width = 0.05,color = 'r')
ax.arrow(1,2,2,0.5,length_includes_head = True,
             head_length = 0.1,head_width = 0.05,color = 'r')


ax.text(3,2.7,"(3,2.5)")
ax.text(1,2.2,"(1,2)")
plt.show()
