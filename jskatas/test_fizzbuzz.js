QUnit.test("returns 1 when given 1", function(assert) {
	var result = fizzbuzzer(1);
	assert.equal(result, 1);
});

QUnit.test("returns 2 when given 2", function(assert) {
	var result = fizzbuzzer(2);
	assert.equal(result, 2);
});
