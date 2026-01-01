
DROP TABLE IF EXISTS user_events;

-- user_events table
CREATE TABLE user_events (
    event_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    event_type VARCHAR(20) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    session_id VARCHAR(100) NOT NULL,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_event_type CHECK (event_type IN ('view', 'purchase', 'add_to_cart', 'remove_from_cart')),
    CONSTRAINT check_price CHECK (product_price >= 0)
);

-- indexes for better query performance
CREATE INDEX idx_user_id ON user_events(user_id);
CREATE INDEX idx_event_type ON user_events(event_type);


-- a view for purchase analytics
CREATE OR REPLACE VIEW purchase_analytics AS
SELECT 
    DATE(event_timestamp) as purchase_date,
    COUNT(*) as total_purchases,
    SUM(product_price) as total_revenue,
    AVG(product_price) as avg_order_value,
    COUNT(DISTINCT user_id) as unique_customers
FROM user_events
WHERE event_type = 'purchase'
GROUP BY DATE(event_timestamp)
ORDER BY purchase_date DESC, total_revenue DESC;

-- a view for user activity summary
CREATE OR REPLACE VIEW user_activity_summary AS
SELECT 
    user_id,
    COUNT(*) as total_events,
    COUNT(CASE WHEN event_type = 'view' THEN 1 END) as views,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) as purchases,
    COUNT(CASE WHEN event_type = 'add_to_cart' THEN 1 END) as cart_adds,
    SUM(CASE WHEN event_type = 'purchase' THEN product_price ELSE 0 END) as total_spent,
    MAX(event_timestamp) as last_activity
FROM user_events
GROUP BY user_id
ORDER BY total_events DESC;

