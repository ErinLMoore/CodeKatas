QUnit.test("discount must be at least 5% to start promo", function(assert) {
	var expected = true
	var result = discount_not_too_low(1, .5);
	assert.equal(result, true);
	var expected = false
	var result =  discount_not_too_low(1, .97);
	assert.equal(result, false);
});

QUnit.test("discount must be %30 or under to start promo", function(assert) {
	var expected = true
	var result = discount_not_too_high(1, .5);
	assert.equal(result, true);
	var expected = false
	var result = discount_not_too_high(1, .2);
	assert.equal(result, false);
});
