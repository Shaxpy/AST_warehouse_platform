# Requirements
Please fill in your requriements in the following format, following the EARS approach. The fill ins should be in *italic* or **bold** form, according to the template.
## Ubiquitous
- The *robotic system* shall be able to **store arriving merchandise on shelves, dispatch items on request by an arriving order, and throw away old items to make room for new items on demand.**
- The *robotic system* shall be able to **carefully inventory items to ensure that the order management system is always aware of the current stock.**
- The *robotic system* shall be able to **operate in a multi-robot system, with each individual robot handling one item at a time.**
- The robots shall only handle items on the delivery ports, the trash, and the dispatchers when stepping on top of a marker.
- The robots shall be able to return to their charging docks when not in use to avoid blocking the way for other robots and human personnel.

## Event-driven
-WHEN *new items arrive at the delivery ports*, the *robotic system* shall **store the items on the shelves and update the inventory**.
-WHEN *an order is received*, the *robotic system* shall **dispatch the requested items to the appropriate dispatcher.**
-WHEN *old items need to be thrown away to make room for new items*, the *robotic system* shall **identify the oldest items and dispose of them.**
-WHEN *human personnel are on site to perform repairs, inspections, or other duties like cleaning*, the *robotic system* shall **adjust its operations to avoid interfering with their work.**
## Unwanted behaviour
- IF *a robot attempts to enter a "no-go" area, such as the fire doors*, THEN the *robotic system* shall **prevent the robot from entering and alert human personnel.**
- IF *a robot drops a heavy item*, THEN the *robotic system* shall **immediately stop the robot and alert human personnel.**
## State-driven
- WHILE *`<system state>`*, the *`<system name>`* shall *`<system
response>`*
-WHILE the *robotic system is in operation*, the *robots* shall **continuously monitor their battery levels and return to their charging docks when necessary.**
-WHILE the *robotic system is in operation*, the *order management system* shall **continuously update the inventory based on the items stored on the shelves.**
## Optional feature
- WHERE the *robotic system includes a feature for remote monitoring and control*, the *robotic system* shall **allow authorized personnel to monitor and control the system from a remote location.**
## Complex
- The *robotic system* shall be able to **handle multiple orders simultaneously and prioritize them based on their urgency.**
- The *robotic system* shall be able to **adapt to changes in the layout of the warehouse, such as the addition or removal of shelves.**
- The *robotic system* shall be able to **handle items of different shapes and sizes, and adjust its operations accordingly.**
