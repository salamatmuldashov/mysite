1. Architecture Overview
Main Service:

    Responsible for handling product management, categories, wishlist, and other product-related features.
    Provides API endpoints for creating, updating, deleting, and retrieving products, categories, and wishlists.
    
Order Service:
    Responsible for handling order processing, including creating and updating orders, managing order items, payment processing.
    

Communication:
    Both services communicate via HTTP using RESTful APIs. The Order Service makes requests to the Main Service to fetch user details when creating order to check for user exist and other validation aims

Database:

    Each service has its own isolated database built via PostgreSQL

I provided application architecture below

    +---------------------+        +--------------------+
    |    Main Service     |        |    Order Service    |
    | (Product Management,|        | (Order Processing,  |
    | Categories, Wishlist)|        | Payment Processing) |
    +---------------------+        +--------------------+
            |                          |
    +--------+--------+                 |
    | Product APIs    |                 |    +----------------------+
    | Categories APIs |                 +----> Order APIs           |
    | Wishlist APIs   |                      |                      |
    |   Other APIs    |                      +----------------------+
    +-----------------+                                    |
                |                                           |
                |                                           |
                |                                           |
        +--------------------+                  +--------------------+         
        | PostgreSQL Database|                  | PostgreSQL Database|  
        |   (Main DB)        |                  |      (Order DB)    |   
        +--------------------+                  +--------------------+     
