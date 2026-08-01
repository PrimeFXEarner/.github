/**
 * PrimeFXEarner Risk Management Library
 */
const calculatePositionSize = (balance, riskPercent, stopLossPips, pipValue) => {
    if (balance <= 0 || riskPercent <= 0 || stopLossPips <= 0) {
        throw new Error("All input values must be positive.");
    }
    const riskAmount = balance * (riskPercent / 100);
    const positionSize = riskAmount / (stopLossPips * pipValue);
    return { riskAmount: riskAmount.toFixed(2), positionSize: positionSize.toFixed(2) };
};

module.exports = { calculatePositionSize };