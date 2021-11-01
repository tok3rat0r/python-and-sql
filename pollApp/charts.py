import matplotlib.pyplot as plt


def chart_poll_votes(options):
    figure = plt.figure()
    axes = figure.add_subplot()

    axes.pie(
        [len(option.votes) for option in options],
        labels=[option.text for option in options],
        autopct="%1.1f%%"
    )

    return figure


def create_bar_chart(polls):
    figure = plt.figure(figsize=(5, 4))
    figure.subplots_adjust(bottom=0.3)
    axes = figure.add_subplot()

    axes.bar(
        range(len(polls)),
        [poll[1] for poll in polls],
        tick_label=[poll[0] for poll in polls]
    )
    plt.xticks(rotation=40, ha="right")

    return figure
