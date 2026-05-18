CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50),
    kyc_status VARCHAR(20),
    risk_category VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    account_type VARCHAR(30),
    balance DECIMAL(15,2),
    account_status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,

    sender_account INT,
    receiver_account INT,

    amount DECIMAL(15,2),

    transaction_type VARCHAR(30),

    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    location VARCHAR(100),

    device_id VARCHAR(100),

    ip_address VARCHAR(50),

    is_suspicious BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (sender_account) REFERENCES accounts(account_id),

    FOREIGN KEY (receiver_account) REFERENCES accounts(account_id)
);

CREATE TABLE alerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,

    transaction_id INT,

    alert_type VARCHAR(50),

    risk_score DECIMAL(5,2),

    alert_status VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (transaction_id)
    REFERENCES transactions(transaction_id)
);