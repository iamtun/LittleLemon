# LittleLemon
Little Lemon Restaurant

# LittleLemon
Little Lemon Restaurant

## API Endpoints

### Menu
- `GET /restaurant/menu/` - List all menu items
- `POST /restaurant/menu/` - Create a new menu item
- `GET /restaurant/menu/<int:pk>` - Retrieve a specific menu item
- `PUT /restaurant/menu/<int:pk>` - Update a specific menu item
- `DELETE /restaurant/menu/<int:pk>` - Delete a specific menu item

### Booking
- `GET /restaurant/booking/` - List all bookings
- `POST /restaurant/booking/` - Create a new booking
- `GET /restaurant/booking/<int:pk>` - Retrieve a specific booking
- `PUT /restaurant/booking/<int:pk>` - Update a specific booking
- `DELETE /restaurant/booking/<int:pk>` - Delete a specific booking

### Authentication
- `POST /api-token-auth/` - Obtain authentication token