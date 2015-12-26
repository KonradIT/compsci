##Parallel vs Serial

####Parallel:

Multiple threads at the same time.

####Serial:

One thread is started and until it finishes there is no other thread

###Data transmission:

* **Parallel**: Multiple bits sent at the same time
* **Serial**: One bit at a time

####Well, why even bother with serial when parallel exists?

* Multiple threads at once? Yeah, but wait for the corruption of data that can happen over long distance cause the line cannot hold that much data.
* For parallel, more expensive hardware is needed to send all that data in one go.
* Also, it might be out of sync / order.

####When to use parallel or serial:

* **Parallel**: using USB/printer or other peripherical devices.
* **Serial**: computer <---> modem


