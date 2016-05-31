
max_promo_length = 30
min_discount_percent = .05
max_discount_percent = .3
price_stability_length_required = 30
date_offset = (24*60*60*1000) * price_stability_length_required
todays_date = new Date()

function Store(){
item0 = new Item(new Date(todays_date.getDate()-45), 1)
item1 =	new Item(new Date(todays_date.getDate()-15), 1)
this.items = [];
this.items.push(item0)
this.items.push(item1)
this.promos = [];

this.add_promo = function(promo, item) {
  if (validate_promo(promo, item)){
    item.underredpencil = true;
    update_promo(item, promo);
    change_item_price(item, promo.newprice);
    item.dateoflastchange = todays_date;
    this.promos.push(promo);
    }
  }
}

function validate_promo(promo, item){
  this.item = item
  var is_valid =discount_in_right_range(item.currentprice, promo.newprice) &&
    promo_length_valid(promo.enddate)&&
    price_stable_long_enough(item.dateoflastchange)&!
    item.underredpencil                                                                              ;

    return is_valid
}

function change_item_price(item, newprice){
  if( newprice > item.currentprice){
    item.underredpencil = false;
  }
  item.currentprice = newprice;
}

function update_promo(item, promo){
  promo.item = item;
  promo.originalprice = item.currentprice;
}
function discount_in_right_range(oldprice, newprice){
  return discount_not_too_low(oldprice, newprice)&&
          discount_not_too_high(oldprice, newprice);
}

function promo_length_valid(enddate){
  var diff = time_difference_in_days(todays_date, enddate);
  return (diff <=date_offset);
}

function price_stable_long_enough(dateoflastchange){
    var diff = time_difference_in_days(todays_date, dateoflastchange);
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

function time_difference_in_days(time1, time2){
  time1_ms = time1.getTime();
  time2_ms = time2.getTime();
  return  Math.abs(time1_ms-time2_ms);

}
