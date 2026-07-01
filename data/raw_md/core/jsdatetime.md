---
description: 지도 내 시간 설정을 위한 API 입니다.
---

# JSDateTime

> Module.JSDateTime() API를 생성합니다.

```javascript
var startTime = new Module.JSDateTime(2023, 4, 27, 8, 0, 0); // year, month, day, hour, minute, second
```

## properties

| Name   | Type   | Description |
| :----- | :----- | :---------- |
| year   | number | 년도.       |
| month  | number | 월.         |
| day    | number | 일.         |
| hour   | number | 시간.       |
| minute | number | 분.         |
| second | number | 초          |

## Function

### setCurrentTime()

> 현재 시간을 기반으로 시간을 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

{% endtab %}
{% tab title="Template" %}

```javascript
var startTime = new Module.JSDateTime();
startTime.setCurrentTime();
```

{% endtab %}
{% endtabs %}
