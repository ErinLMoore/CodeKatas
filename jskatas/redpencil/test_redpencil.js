
QUnit.test("discount must be at least 5% to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_low(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result =  discount_not_too_low(1, .97);
	assert.equal(result, expected);
});

QUnit.test("discount must be %30 or under to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_high(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_not_too_high(1, .2);
	assert.equal(result, expected);
});

QUnit.test("discount in right range", function(assert) {
	var expected = true
	var result = discount_in_right_range(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_in_right_range(1, .97);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_in_right_range(1, .05);
	assert.equal(result, expected);
});

QUnit.test("price_stable_for_30_days", function(assert) {
	last_change_date = new Date(2016,2,10);
	item = new Item(last_change_date);
	var expected = true;
	var result = price_stable_long_enough(item);
	assert.equal(result, expected);


	last_change_date = new Date(2016,4,1);
	item = new Item(last_change_date);
	var expected = false;
	var result = price_stable_long_enough(item);
	assert.equal(result, expected);
});


QUnit.test("promo length 30 days or less", function(assert) {
	enddate = new Date(2016,4,16);
	var expected = true
	var result = promo_length_valid(enddate);
assert.equal(result, expected);
enddate = new Date(2016,5,16);
	var expected = false
	var result = promo_length_valid(enddate);
assert.equal(result, expected);
});
