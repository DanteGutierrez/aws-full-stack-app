# aws-full-stack-app
Creating a Full stack application using full cloud based tools 

# Backend #
Using aws lambda functions to connect to the api gateway
- Language: Python
- Full CRUD

## Structure: ##
### Books ###

Field | Data Type
------|----------
picture | string
title | string
author | string
genre | enum
price | number
rent_price | number
past_users | dict<date, user_id>
condition | enum
is_hardback | boolean
availability | enum
owner | dict<date, user_id>

### Users ###

Field | Data Type
------|----------
name | string
password | string
email | string
address | string
payment | dict<user_id, card_id>
role | enum
rented | dict<date, book_id>
owned | dict<date, book_id>

### Receipts ###

Field | Data Type
------|----------
user_id | string
date | date
cost | number
purchases | list[purchase OBJ]
payment_id | string

#### Purchase OBJ ####
* Not a collection

Field | Data Type
------|----------
book_id | string
price | number
is_owned | boolean


## API Documentation ##

Endpoint | Body | Returns | Notes
---------|------|---------|------
