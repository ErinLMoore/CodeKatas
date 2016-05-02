
max_promo_length = 30
min_discount_percent = .05
max_discount_percent = .3
price_stability_length_required = 30
date_offset = (24*60*60*1000) * price_stability_length_required
todays_date = new Date(2016,4,15)

function discount_in_right_range(oldprice, newprice){
  return discount_not_too_low(oldprice, newprice)&&
          discount_not_too_high(oldprice, newprice);
}

function promo_length_valid(startdate){
  diff = Math.abs(todays_date-startdate)
  return (diff <=date_offset);
}

function price_stable_long_enough(item){
    diff = Math.abs(todays_date-item.dateoflastchange)
    return (diff >=date_offset);
}

function  discount_not_too_low(oldprice, newprice) {
  var result = ((oldprice-newprice )>=oldprice*min_discount_percent);
  return result;
}

function discount_not_too_high(oldprice, newprice){
  var result = ((oldprice*max_discount_percent)<=newprice);
  return result;
}

function price_has_been_stable_30_days(item){
  return ((todays_date - item.dateoflastchange)>=30)
}
