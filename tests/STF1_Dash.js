import { Selector } from 'testcafe';

fixture `New Fixture`
    .page `http://127.0.0.1:8050/`;

test('New Test', async t => {
    await t
        .click(Selector('#react-entry-point h1').withText('STF1 Data Analysis'))
        .expect(Selector('#react-entry-point h1').withText('STF1 Data Analysis').textContent).eql('STF1 Data Analysis')
        .click(Selector('#react-select-2--value div').withText('Temprature X axis'))
        .click('#demo-dropdown .Select-arrow-zone')
        .click('#demo-dropdown .Select-arrow')
        .click(Selector('#react-select-2--list div').withText('Magnetometer X axis').nth(3))
        .expect(Selector('#dd-output-container div').withText('1.5M').nth(3).id).eql("")
        .click(Selector('#dd-output-container div').withText('1.5M').nth(3));
});