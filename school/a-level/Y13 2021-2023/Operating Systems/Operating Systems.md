#  Operating Systems

## The Kernel

The kernel is the central module of an OS. It is the part of the operating system that loads first, and it remains in memory - usually in a protected area. Typically, it is responsible for management of the CPU and memory.

The kernel connects the system hardware to the application software. The Linux kernel is used in numerous operating systems including Android, Ubuntu, and firmware for devices such as routers.

## Types of Operating Systems

### Single User - Single Application

Only has to deal with one person running one application at a time. For example, a Nokia brick.

### Single User - Multi-application

Only has to deal with one person, but must be able to handle running multiple applications concurrently. For example, Android tablets.

### Multi-user - Multi-tasking

Must be able to handle multiple users running multiple applications concurrently. For example, Windows as you can stay logged in as many different users who have different states on the computer simultaneously.

### Real-Time

Real-Time operating systems must process tasks in a set time which is critical to it's operation. These are not needed in computers, but may be needed in something like a car which has to react incredibly quickly to prevent accidents.

### Batch-Op

A batch is a small job repeated many times. For each iteration, a small change is made to the data; for example, printing gas bills/bank statements. They are designed to be left running with little user interactions.

## Process Manager

The process manager is a part of the kernel. Jobs can consist of many processes (one-to-many). This is the job of the process scheduler.

### Process States

- HOLD
- READY
- RUNNING
- WAIT
- FINISHED/FAIL
