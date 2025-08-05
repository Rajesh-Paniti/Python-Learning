from string import Template

message = Template('$name, your ticket number is $number')
ticket_data = message.substitute(name = "Rajesh", number = "139206")

print(ticket_data)