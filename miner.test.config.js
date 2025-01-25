module.exports = {
  apps: [
    {
      name: 'miner',
      interpreter: 'python3',
      script: './neurons/miner.py',
      args: '--netuid 247 --logging.debug --logging.trace --subtensor.network test --wallet.name Tensorplex --wallet.hotkey synapz-SN38miner-1 --axon.port 8091 --blacklist.validator.min_stake 0',
      env: {
        PYTHONPATH: '.'
      },
    },
  ],
};
