def apply_discount(price: int, rate: float) -> int:
    """정가에 할인율을 적용한 금액 반환. rate는 0~1 사이."""
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")
    return int(price * (1 - rate))


def main():
    print(f"10000원 20% 할인 → {apply_discount(10000, 0.2)}원")


if __name__ == "__main__":
    main()
