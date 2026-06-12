import logging

# 1. Sửa cấu hình logging để hiển thị mức DEBUG
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_discount_rate(tier: str, quantity: int) -> float:
    """Trả về tỷ lệ chiết khấu dựa trên hạng thành viên và số lượng"""
    logger.debug(f"Đang tính toán chiết khấu cho hạng {tier} với số lượng {quantity}")
    
    # 2. Xử lý ngoại lệ chặt chẽ (Clean Code): trả ra ValueError
    if quantity <= 0:
        logger.error(f"Số lượng sản phẩm không hợp lệ: {quantity}")
        raise ValueError("Quantity must be positive")

    # Xác định tỷ lệ chiết khấu cơ bản
    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        rate = 0.0
        
    # 3. Sửa lỗi LOGIC: Sử dụng += để cộng dồn chiết khấu thưởng thêm
    if quantity >= 50:
        rate += 0.05  # Thưởng thêm 5% thay vì ghi đè
        logger.debug(f"Đã cộng thêm chiết khấu số lượng lớn cho {tier}")
        
    return rate

def calculate_agency_total(price: float, quantity: int, tier: str) -> float:
    """Tính tổng tiền sau chiết khấu cho đại lý"""
    if price < 0:
        raise ValueError("Đơn giá không được âm")
        
    try:
        rate = get_discount_rate(tier, quantity)
        final_price = price * (1 - rate) * quantity
        logger.info(f"Kết quả: Tổng tiền = {final_price:.2f} (Rate: {rate*100}%)")
        return final_price
    except ValueError as e:
        logger.error(f"Lỗi tính toán: {e}")
        raise

# Code chạy thử
if __name__ == "__main__":
    print("--- Case 1: Kiểm tra lỗi logic biên (Hạng Gold, SL 50) ---")
    calculate_agency_total(100, 50, "gold")  
    
    print("\n--- Case 2: Kiểm tra dữ liệu đầu vào (SL -5) ---")
    try:
        calculate_agency_total(100, -5, "silver")
    except ValueError:
        print("Đã chặn thành công dữ liệu đầu vào sai.")