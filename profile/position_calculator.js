const calculatePositionSize = (balance, riskPercent, stopLossPips, pipValue) => {
    const riskAmount = balance * (riskPercent / 100);
    const positionSize = riskAmount / (stopLossPips * pipValue);
    return { riskAmount: riskAmount.toFixed(2), positionSize: positionSize.toFixed(2) };
};
module.exports = { calculatePositionSize };
