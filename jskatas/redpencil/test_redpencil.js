
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
	var expected = true
	var result = price_stable_long_enough(311, 350);
	assert.equal(result, expected);
	var expected = false
	var result = price_stable_long_enough(311, 312);
	assert.equal(result, expected);
});


QUnit.test("promo length 30 days or less", function(assert) {
	var expected = true
	var result = promo_length_valid(311, 312);
assert.equal(result, expected);
	var expected = false
	var result = promo_length_valid(311, 350);
assert.equal(result, expected);
});

QUnit.test("item exists?", function(assert) {
	var expected = 1
	var result = item_exists(1);
	assert.equal(result, expected);
	});
