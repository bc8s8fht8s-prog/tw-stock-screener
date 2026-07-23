"""
TW Stock Screener
System Configuration
"""

# ===== App =====
APP_NAME = "TW Stock Screener"
VERSION = "1.0.0"

# ===== Schedule =====
UPDATE_TIME = "15:10"

# ===== MACD =====
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# ===== OSC =====
# None = 不設限
# 1 = -1 ~ +1
# 2 = -2 ~ +2
# 3 = -3 ~ +3
OSC_RANGE = None

# ===== Log =====
ENABLE_LOG = True

# ===== Market =====
INCLUDE_TWSE = True      # 上市
INCLUDE_TPEX = True      # 上櫃
INCLUDE_KY = True        # KY股

EXCLUDE_ETF = True
EXCLUDE_ETN = True
EXCLUDE_WARRANT = True
EXCLUDE_PREFERRED = True
EXCLUDE_EMERGING = True

# ===== Development =====
TEST_MODE = False

TEST_LIMIT = 10

# 正式掃描時使用
FULL_SCAN_DELAY = 0