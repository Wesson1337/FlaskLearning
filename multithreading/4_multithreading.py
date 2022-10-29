import logging
import random
import threading
import time

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            logger.info(f'Philosopher {self.name} starts thinking')
            time.sleep(random.randint(1, 5))
            logger.info(f'Philosopher {self.name} is hungry.')
            try:
                self.left_fork.acquire()
                time.sleep(random.randint(1, 5))
                logger.info(f'Philosopher {self.name} acquired left fork')
                if self.right_fork.locked():
                    continue
                try:
                    self.right_fork.acquire()
                    logger.info(f'Philosopher {self.name} acquired right fork')
                    self.dinning()
                finally:
                    self.right_fork.release()
            finally:
                self.left_fork.release()

    def dinning(self):
        logger.info(f'Philosopher {self.name} starts eating')
        time.sleep(random.randint(1, 5))
        logger.info(f'Philosopher {self.name} finishes eating and leaves to think')


def main():
    forks = [threading.Lock() for _ in range(5)]

    philosophers = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5]) for i in range(5)
    ]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(200)
    Philosopher.running = False
    logger.info("Now we're finishing..")


if __name__ == '__main__':
    main()