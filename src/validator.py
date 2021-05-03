import numpy
import pandas as pd

import src.helpers.violation_rules as rules


class Validator:
    def __init__(self, data="", image=""):
        self._data = data
        self._image = image

    def _get_measurement_data(self):
        return self._data

    def _set_measurement_data(self, data):
        self._data = data

    @staticmethod
    def _response_output(processed_data: list, violation_rule: str) -> dict:
        """Formats response for validator

        Returns
        -------
            validator response json string
        """
        return {"violation_rule": violation_rule, "data": processed_data}

    def multiple_crop_measurements(self) -> dict:
        """Returns multiple measurements with same crop and farm

        Returns
        -------
            multiple measurements with same crop and farm
        """
        measurement_data = self._get_measurement_data()
        filtered_measurement_data = []
        df = pd.DataFrame(measurement_data)
        df_grouped = df.groupby(["farm_id", "crop"], as_index=False).size()
        multiple_occurance = df_grouped.loc[df_grouped["size"] > 1]
        mutiple_measurement_instances = multiple_occurance.to_dict("records")

        for i in range(len(mutiple_measurement_instances)):
            filtered_df = df[
                df["farm_id"] == mutiple_measurement_instances[i]["farm_id"]
            ]
            filtered_measurement_data += filtered_df.to_dict("records")

        return Validator._response_output(
            processed_data=filtered_measurement_data,
            violation_rule=rules.MULTIPLE_MEASUREMENTS_VIOLATION,
        )

    def validate_weight(self) -> dict:
        """Compares dry and wet weight of crops

        Returns
        -------
            crops with dry weight greater than wet weight
        """
        updated_measurement_data = []
        measurement_data = self._get_measurement_data()

        for i in range(len(measurement_data)):
            current_wet_weight = measurement_data[i]["wet_weight"]
            current_dry_weight = measurement_data[i]["dry_weight"]

            temp_measurement = {
                key: value
                for (key, value) in measurement_data[i].items()
                if current_dry_weight > current_wet_weight
            }

            if bool(temp_measurement):
                updated_measurement_data.append(temp_measurement)

        return Validator._response_output(
            processed_data=updated_measurement_data,
            violation_rule=rules.DRY_WEIGHT_VIOLATION,
        )

    def validate_dry_weight(self) -> dict:
        """Validate dry weight via standard deviation

        Returns
        -------
            crops with dry weight outlier

        """
        updated_measurement_data = []
        measurement_data = self._get_measurement_data()
        dry_weight_list = [
            measurement_data[i]["dry_weight"] for i in range(len(measurement_data))
        ]
        dry_weight_std = numpy.std(dry_weight_list, axis=0)
        dry_weight_mean = numpy.mean(dry_weight_list, axis=0)
        positive_one_std_mean = dry_weight_mean + 1 * dry_weight_std
        negative_one_std_mean = dry_weight_mean - 1 * dry_weight_std

        for i in range(len(measurement_data)):
            current_dry_weight = measurement_data[i]["dry_weight"]
            temporary_measurement = {
                key: value
                for (key, value) in measurement_data[i].items()
                if current_dry_weight < negative_one_std_mean
                or current_dry_weight > positive_one_std_mean
            }

            if bool(temporary_measurement):
                updated_measurement_data.append(temporary_measurement)
        return Validator._response_output(
            processed_data=updated_measurement_data,
            violation_rule=rules.DRY_WEIGHT_OUTLIER_VIOLATION,
        )

    def validate_farm_distance(self):
        pass

    def validate_photos(self):
        pass
