import mysql.connector

def get_db_connection():
    """Establish a database connection and return the connection object."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vikas@5599',
        database='Time2order'
    )

def get_pending_vendors():
    """Fetch all pending vendors from the yettoapprove table."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM yettoapprove")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_vendor_by_id(vendor_id):
    """Fetch a vendor by their ID from the yettoapprove table."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM yettoapprove WHERE id = %s", (vendor_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_into_vendors(vendor):
    """Insert a new vendor into the vendors table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vendors (username, password, mobile_number, email, shop_name, shop_owner_name, map_link, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        vendor['username'], vendor['password'], vendor['mobile_number'],
        vendor['email'], vendor['shop_name'], vendor['shop_owner_name'],
        vendor['map_link'], vendor['category']
    ))
    conn.commit()
    cursor.close()
    conn.close()

def insert_into_rejectedlist(vendor):
    """Insert a vendor into the rejectedlist table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO rejectedlist (username, password, mobile_number, email, shop_name, shop_owner_name, map_link, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        vendor['username'], vendor['password'], vendor['mobile_number'],
        vendor['email'], vendor['shop_name'], vendor['shop_owner_name'],
        vendor['map_link'], vendor['category']
    ))
    conn.commit()
    cursor.close()
    conn.close()

def delete_from_yettoapprove(vendor_id):
    """Delete a vendor from the yettoapprove table by their ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM yettoapprove WHERE id = %s", (vendor_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_vendors():
    """Fetch all vendors from the vendors table."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vendors")
    vendors = cursor.fetchall()
    cursor.close()
    conn.close()
    return vendors

def get_products_by_vendor(vendor_username):
    """Fetch products associated with a specific vendor."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE vendor_id = %s", (vendor_username,))
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def get_vendorapproved_by_id(vendor_id):
    """Fetch a vendor by their ID from the yettoapprove table."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vendors WHERE id = %s", (vendor_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result