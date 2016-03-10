QUnit.test("returns 1 when given 1", function(assert) {
	var result = fizzbuzzer(1);
	assert.equal(result, 1);
});

QUnit.test("returns 2 when given 2", function(assert) {
	var result = fizzbuzzer(2);
	assert.equal(result, 2);
});

QUnit.test("returns Fizz when given 3", function(assert) {
	var result = fizzbuzzer(3);
	assert.equal(result, 'Fizz');
});

QUnit.test("returns Fizz when given 6", function(assert) {
	var result = fizzbuzzer(6);
	assert.equal(result, 'Fizz');
});

QUnit.test("returns Buzz when given 10", function(assert) {
	var result = fizzbuzzer(10);
	assert.equal(result, 'Buzz');
});

QUnit.test("returns FizzBuzz when given 60", function(assert) {
	var result = fizzbuzzer(60);
	assert.equal(result, 'FizzBuzz');
});
