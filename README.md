# mini-hackathon

# Soko Hub MVP

## Simplified Concept

A minimal marketplace where vendors can list products and customers can browse and place orders. Focus: Get something working end-to-end quickly.

**Core User Stories:**
1. As a vendor, I can register and list products for sale
2. As a customer, I can browse products and place an order
3. As a vendor, I can see orders for my products

**Out of Scope for MVP:**
- Payment integration
- Reviews and ratings
- Email notifications
- Image galleries (single image only)
- Advanced search/filters
- Shopping cart (direct checkout)
- Admin dashboard
- Password reset
- Profile editing

---

## Module 1: Project Setup & Database Models

### Task 1.1: Initial Project Setup
**Deliverable:** Working Django project with database connected

**Acceptance Criteria:**
- [ ] Django project created with name 'sokohub'
- [ ] Three apps created: accounts, products, orders
- [ ] PostgreSQL or SQLite database configured and connected
- [ ] All apps registered in INSTALLED_APPS
- [ ] Development server runs without errors
- [ ] Bootstrap CDN added to base template
- [ ] Static and media directories configured

### Task 1.2: Database Models
**Deliverable:** All core models defined and migrated

**Acceptance Criteria:**
- [ ] Custom User model with user_type field (choices: 'vendor', 'customer')
- [ ] User model includes: phone, location fields
- [ ] Product model with: vendor (FK), name, description, price, stock, image, status, created_at
- [ ] Order model with: customer (FK), total, status, delivery_address, phone, created_at
- [ ] OrderItem model with: order (FK), product (FK), quantity, price
- [ ] All models have __str__ methods
- [ ] Database migrations created and applied successfully
- [ ] Sample data can be created via Django shell

### Task 1.3: Admin Registration (15 min)
**Deliverable:** All models accessible via Django admin

**Acceptance Criteria:**
- [ ] All models registered in admin.py
- [ ] User model shows user_type in list display
- [ ] Product model shows name, vendor, price, stock in list display
- [ ] Order model shows customer, total, status, created_at in list display
- [ ] Superuser created for testing
- [ ] Admin interface accessible and functional

---

## Module 2: Authentication & User Management

### Task 2.1: User Registration 
**Deliverable:** Users can register as vendor or customer

**Acceptance Criteria:**
- [ ] Registration form includes: username, email, password, confirm password, user_type (dropdown), phone, location
- [ ] Form validates: required fields, email format, password match, password min 8 characters
- [ ] User_type dropdown shows "Vendor" and "Customer" options
- [ ] Successful registration creates user in database
- [ ] User automatically logged in after registration
- [ ] Vendors redirected to vendor dashboard
- [ ] Customers redirected to product listing page
- [ ] Error messages displayed for validation failures
- [ ] Registration page styled with Bootstrap

### Task 2.2: Login & Logout 
**Deliverable:** Users can login and logout

**Acceptance Criteria:**
- [ ] Login form with username and password fields
- [ ] "Remember me" checkbox (optional)
- [ ] Successful login redirects based on user_type
- [ ] Invalid credentials show clear error message
- [ ] Logout button in navigation bar
- [ ] Logout clears session and redirects to homepage
- [ ] Login required decorator works on protected views
- [ ] "Next" parameter redirects after login

### Task 2.3: Access Control 
**Deliverable:** Role-based access restrictions

**Acceptance Criteria:**
- [ ] @vendor_required decorator created and functional
- [ ] @customer_required decorator created and functional
- [ ] Unauthenticated users redirected to login page
- [ ] Vendors cannot access customer-only pages
- [ ] Customers cannot access vendor-only pages
- [ ] Clear error message for unauthorized access
- [ ] Applied to vendor dashboard, add product, and checkout views

### Task 2.4: Navigation & User Context 
**Deliverable:** Dynamic navigation based on user state

**Acceptance Criteria:**
- [ ] Logged-out users see: Home, Products, Login, Register
- [ ] Logged-in customers see: Home, Products, My Orders, Logout
- [ ] Logged-in vendors see: Home, Dashboard, My Products, Orders, Logout
- [ ] User's name displayed in navigation when logged in
- [ ] Active page highlighted in navigation
- [ ] Mobile-responsive hamburger menu

---

## Module 3: Product Management (Vendor Side)

### Task 3.1: Vendor Dashboard
**Deliverable:** Overview page for vendors

**Acceptance Criteria:**
- [ ] Protected by @vendor_required decorator
- [ ] Shows count of total products
- [ ] Shows count of active products
- [ ] Shows count of out-of-stock products
- [ ] Shows count of pending orders (orders containing vendor's products)
- [ ] Displays 5 most recent products in cards
- [ ] "Add New Product" button prominently displayed
- [ ] "View All Products" link
- [ ] "View Orders" link
- [ ] Grid layout with Bootstrap cards
- [ ] Responsive design

### Task 3.2: Add Product
**Deliverable:** Vendors can create new products

**Acceptance Criteria:**
- [ ] Form includes: name, description, price, stock quantity, image upload
- [ ] Price field validates positive decimal numbers
- [ ] Stock field validates non-negative integers
- [ ] Description textarea has reasonable size
- [ ] Image upload accepts JPEG/PNG only (or skip if time-constrained)
- [ ] Product automatically assigned to logged-in vendor
- [ ] Product status defaults to 'active'
- [ ] Success message shown after creation
- [ ] Redirects to vendor's product list
- [ ] Validation errors displayed inline
- [ ] Form styled with Bootstrap

### Task 3.3: Product List (Vendor View)
**Deliverable:** Vendors can view all their products

**Acceptance Criteria:**
- [ ] Shows only products belonging to logged-in vendor
- [ ] Displays in table or card grid format
- [ ] Each product shows: image thumbnail, name, price, stock, status
- [ ] Stock quantity highlighted if zero (out of stock)
- [ ] "Add New Product" button at top
- [ ] Products sorted by newest first
- [ ] Shows "No products yet" message if empty
- [ ] Pagination if time allows (optional)

---

## Module 4: Product Browsing (Customer Side)

### Task 4.1: Homepage 
**Deliverable:** Landing page with product preview

**Acceptance Criteria:**
- [ ] Hero section with marketplace name and tagline
- [ ] "Browse Products" call-to-action button
- [ ] Shows 6-8 newest active products
- [ ] Each product card displays: image (or placeholder), name, price, vendor name
- [ ] "View Details" button on each card
- [ ] Grid layout: 1 column mobile, 2-3 columns tablet, 3-4 columns desktop
- [ ] Visually appealing with Bootstrap styling
- [ ] Fast loading (under 2 seconds)

### Task 4.2: Product Listing Page
**Deliverable:** Browse all available products

**Acceptance Criteria:**
- [ ] Shows all products with status='active'
- [ ] Products displayed in responsive grid
- [ ] Each card shows: image, name, price, vendor name, stock status
- [ ] Out-of-stock items clearly marked and "Buy Now" disabled
- [ ] Click on card navigates to product detail page
- [ ] Basic sorting: newest first (default), price low-to-high, price high-to-low
- [ ] Simple category filter if time allows (optional)
- [ ] Shows "No products available" if empty
- [ ] Pagination showing 12 products per page

### Task 4.3: Product Detail Page 
**Deliverable:** Detailed view of single product

**Acceptance Criteria:**
- [ ] Large product image (or placeholder)
- [ ] Product name as heading
- [ ] Full product description
- [ ] Price prominently displayed
- [ ] Vendor name with link to vendor's products (bonus)
- [ ] Stock status clearly shown
- [ ] Quantity selector (dropdown: 1 to available stock)
- [ ] "Buy Now" button (proceeds to checkout)
- [ ] Button disabled if out of stock
- [ ] "Back to Products" link
- [ ] Breadcrumb navigation
- [ ] Responsive layout

---

## Module 5: Order System

### Task 5.1: Simple Checkout 
**Deliverable:** Customer can place an order for a product

**Acceptance Criteria:**
- [ ] Accessible from "Buy Now" on product detail page
- [ ] Requires user to be logged in as customer
- [ ] Shows order summary: product name, quantity, unit price, total
- [ ] Form collects: delivery address, phone number
- [ ] Form pre-fills user's location if available
- [ ] Validates all required fields
- [ ] "Place Order" button creates Order and OrderItem records
- [ ] Order total calculated automatically
- [ ] Product stock decremented by quantity ordered
- [ ] Success message shown after order placed
- [ ] Redirects to order confirmation page
- [ ] Shows unique order number

### Task 5.2: Order Confirmation
**Deliverable:** Customer sees confirmation after ordering

**Acceptance Criteria:**
- [ ] Shows order number prominently
- [ ] Displays order details: product, quantity, price, total
- [ ] Shows delivery address and phone
- [ ] Shows order status (should be 'pending')
- [ ] "View My Orders" button
- [ ] "Continue Shopping" button
- [ ] Thank you message

### Task 5.3: Customer Order History
**Deliverable:** Customers can view their past orders

**Acceptance Criteria:**
- [ ] Protected by login_required
- [ ] Shows all orders for logged-in customer
- [ ] Orders sorted by date (newest first)
- [ ] Each order displays: order number, date, total, status
- [ ] Click order number to view details
- [ ] Status badge color-coded (pending=yellow, completed=green)
- [ ] Shows "No orders yet" if empty
- [ ] "Continue Shopping" button

### Task 5.4: Vendor Order Management
**Deliverable:** Vendors can see orders for their products

**Acceptance Criteria:**
- [ ] Protected by @vendor_required
- [ ] Shows OrderItems containing vendor's products
- [ ] Each item displays: order number, product name, quantity, customer name, delivery address, status
- [ ] Orders sorted by date (newest first)
- [ ] Status displayed clearly
- [ ] Shows "No orders yet" if empty
- [ ] Basic table layout

---

## Integration & Testing Phase

### Task: End-to-End Testing
**Deliverable:** Working MVP with no critical bugs

**Acceptance Criteria:**
- [ ] Complete vendor flow works: Register → Login → Add Product → View Orders
- [ ] Complete customer flow works: Register → Login → Browse → View Detail → Checkout → View Orders
- [ ] All navigation links work correctly
- [ ] No broken images or CSS
- [ ] No server errors (500)
- [ ] Forms validate properly
- [ ] Database operations work correctly
- [ ] Users redirected appropriately based on role
- [ ] Application responsive on mobile and desktop
- [ ] Can demo complete user journey in under 3 minutes

---

## Deployment Checklist (If Time Allows)

**Acceptance Criteria:**
- [ ] requirements.txt generated with all dependencies
- [ ] README.md with setup instructions created
- [ ] Database migrations committed to version control
- [ ] .gitignore includes venv/, *.pyc, db.sqlite3, .env
- [ ] Sample data script created (optional)
- [ ] Environment variables documented
- [ ] Code pushed to GitHub
- [ ] Quick deploy to Heroku/Railway (bonus)

---

## MVP Success Criteria

At the end of the hours, you should have:

### Functional Requirements
✅ Two types of users can register and login  
✅ Vendors can add products with name, description, price, stock  
✅ Customers can browse all products  
✅ Customers can view product details  
✅ Customers can place orders for products  
✅ Vendors can see orders for their products  
✅ Basic navigation works for all user types  

### Technical Requirements
✅ Django project with 3 apps running  
✅ Database with 5 core models  
✅ Authentication and authorization working  
✅ Forms with validation  
✅ Bootstrap styling throughout  
✅ No critical bugs or errors  

### Demo-Ready
✅ Can register as vendor and add 2-3 products  
✅ Can register as customer and place an order  
✅ Can show vendor seeing the order  
✅ Application looks presentable (not production-ready, but clean)  

---

## What's Intentionally Missing (Post-MVP)

These features are important but excluded to meet the time constraint:

- Shopping cart (multi-product checkout)
- Payment processing
- Product editing/deletion
- Order status updates
- Product images optimization
- Email notifications
- Reviews and ratings
- Search functionality
- Advanced filters
- Vendor profiles
- Customer profiles
- Password reset
- Mobile app
- Analytics dashboard
- Admin moderation
