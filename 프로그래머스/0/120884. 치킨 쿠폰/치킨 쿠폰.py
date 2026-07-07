def solution(chicken):
    answer = 0
    refill_coupon = chicken
    while refill_coupon>=10:
        service_chicken = refill_coupon//10
        answer+=service_chicken
        refill_coupon = (refill_coupon%10) + service_chicken
        
    return answer