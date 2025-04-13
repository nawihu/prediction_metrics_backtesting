"""
Example script demonstrating how to use the Backtester
"""

from prediction_metrics_backtesting import Backtester


def main():
    """Run a sample backtest with the Backtester"""

    # Path to your CSV file (replace with your actual file path)
    csv_path = "sample_data.csv"

    # Create a backtester instance with custom parameters
    backtester = Backtester(
        csv_path=csv_path,
        initial_capital=100000,
        position_size_pct=0.1,  # Use 10% of capital per trade
        take_profit_pct=0.3,  # Take profit at 0.3% gain
        stop_loss_pct=0.2,  # Stop loss at 0.2% loss
        risk_reward_ratio=1.5,
        use_risk_reward_for_tp_sl=True,
        commission_per_trade=0.5,
        slippage_pct=0.005,
        output_dir="example_backtest_results"
    )

    # Run the backtest and generate a report
    metrics = backtester.generate_report()

    # Print key metrics
    print("\nBacktest Results Summary:")
    print(f"Total Return: {metrics['total_return']:.2f}%")
    print(f"Total Trades: {metrics['total_trades']}")
    print(f"Win Rate: {metrics['win_rate']:.2f}%")
    print(f"Profit Factor: {metrics['profit_factor']:.2f}")
    print(f"Max Drawdown: {metrics['max_drawdown']:.2f}%")
    print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")

    # Compare to benchmark
    outperformance = metrics['total_return'] - metrics['benchmark_return']
    print(f"Benchmark Return: {metrics['benchmark_return']:.2f}%")
    print(f"Outperformance: {outperformance:.2f}%")

    print(f"\nDetailed report saved to {backtester.output_dir}/backtest_report.txt")


if __name__ == "__main__":
    main()