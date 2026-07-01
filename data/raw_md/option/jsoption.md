---
description: 지도 내 환경 옵션을 설정하기 위한 API 입니다.
---

# JSOption

> Module.getOption() API를 생성합니다

```javascript
var math = Module.getOption();
```

## Properties

| Name         | Type   | Description                                                                                                                                                    |
| ------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| object_ahead | number | <p>화면 시야 기준 [JSPoint](../object/jspoint.md), HTMLObject 객체 앞 장해물(지형, 시설물) 존재 시 가시화 유무 설정.<br>0: 기본 가시화.<br>1: 장해물 판별.</p> |
|reflect|number|오브젝트 반사 효과 맵 생성 여부|
|backgroundColor|JSColor|지도 기본 배경 색상|

## Funtion

### callBackAddPoint(event) → string

> 측정 기능(거리, 면적 등) 동작 시 마우스 클릭 이벤트에 발생하는 콜백 함수를 추가합니다.
>
> 입력 변수값(event)에서 선언된 매개 변수를 통해 입력된 위치, 이전 위치와의 거리, 총길이를 제공합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| event | function | 콜백 함수.  |

-   Return
    -   "success" : 추가 성공.
    -   "error map load" : 정상적으로 지도가 생성되지 못한 경우.
    -   "error { callback } Undefined" : 콜백 함수가 Undefined으로 입력된 경우.
    -   "error { callback } null" : 콜백 함수가 없는 경우.
    -   "error { callback } Type Mismatch" : 입력된 event가 function 타입이 아닌경우.
-   Sample
    -   the function init 참조.
    -   [Sandbox_Distance Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
function addPoint(e) {
    console.log(e);
}

Module.getOption().callBackAddPoint(addPoint);
```

{% endtab %}
{% endtabs %}

### callBackCompletePoint(event) → string

> 측정 기능(거리, 면적 등) 종료 시 발생하는 콜백 함수를 추가합니다.
>
> 입력 변수값(event)에서 선언된 매개 변수를 통해 측정 객체의 고유 명칭을 제공합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type     | Description |
| :---- | :------- | :---------- |
| event | function | 콜백 함수.  |

-   Return
    -   "success" : 추가 성공.
    -   "error map load" : 정상적으로 지도가 생성되지 못한 경우.
    -   "error { callback } Undefined" : 콜백 함수가 Undefined으로 입력된 경우.
    -   "error { callback } null" : 콜백 함수가 없는 경우.
    -   "error { callback } Type Mismatch" : 입력된 event가 function 타입이 아닌경우.
-   Sample
    -   the function init 참조.
    -   [Sandbox_Distance Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
function endPoint(e) {
    console.log(e);
}

Module.getOption().callBackCompletePoint(endPoint);
```

{% endtab %}
{% endtabs %}

### SetAreaMeasurePolygonDepthBuffer(type) → boolean

> 면적 측정 동작 시 생성된 객체의 depth 설정합니다.
>
> depth 미 설정 시 객체 겹침 시 z-fighting 현상 발생합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                      |
| :--- | :------ | :----------------------------------------------- |
| type | boolean | <p>true: depth 미설정.<br>false: depth 설정.</p> |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the function init 참조.
    -   [Sandbox_Area Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_area)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getOption().SetAreaMeasurePolygonDepthBuffer(false);
// ... or ...
Module.getOption().SetAreaMeasurePolygonDepthBuffer(true);
```

{% endtab %}
{% endtabs %}

### SetDistanceMeasureLineDepthBuffer(type) → boolean

> 거리 측정 동작 시 생성된 객체의 depth 설정합니다.
>
> depth 미 설정 시 객체 겹침 시 z-fighting 현상 발생합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                      |
| :--- | :------ | :----------------------------------------------- |
| type | boolean | <p>true: depth 미설정.<br>false: depth 설정.</p> |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the function init 참조.
    -   [Sandbox_Distance Measurement](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getOption().SetDistanceMeasureLineDepthBuffer(false);
or;
Module.getOption().SetDistanceMeasureLineDepthBuffer(ture);
```

{% endtab %}
{% endtabs %}

### setSlideScreenCount(value) → boolean

> 화면 분할을 설정합니다.
>
> 입력 변수값(value)은 1(단일화면), 2(분할화면) 필수 설정.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description     |
| :---- | :----- | :-------------- |
| value | number | 화면 분활 갯수. |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.

-   Sample
    -   the function setSplitScreen 참조.
    -   [Sandbox_Screen Split](https://sandbox.egiscloud.com/code/main.do?id=effect_screen_split)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getOption().setSlideScreenCount(1);
or;
Module.getOption().setSlideScreenCount(2);
```

{% endtab %}
{% endtabs %}

### setTwoSlideScreenDivideRate(value) → boolean

> 화면 분활 비율을 설정합니다.
>
> 입력 변수값(value)은 0~1 사이 값으로 설정합니다..

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description     |
| :---- | :----- | :-------------- |
| value | number | 화면 비율 설정. |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   the function setSplitScreen 참조.
    -   [Sandbox_Screen Split](https://sandbox.egiscloud.com/code/main.do?id=effect_screen_split)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getOption().setTwoSlideScreenDivideRate(0~1);
```

{% endtab %}
{% endtabs %}

### setTwoSlideScreenLayerList(leftName, rightName) → number

> 분활된 화면에 대해 출력할 레이어를 설정합니다.
>
> 입력 변수값(leftName) 다중 레이어 설정 시 "레이어명칭(1st),레이어명칭(2st)"으로 설정합니다.
>
> 입력 변수값(rightName) 다중 레이어 설정 시 "레이어명칭(1st),레이어명칭(2st)"으로 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description                          |
| :-------- | :----- | :----------------------------------- |
| leftName  | number | 왼쪽 화면 가시화 레이어 명칭 목록.   |
| rightName | number | 오른쪽 화면 가시화 레이어 명칭 목록. |

-   Return
    -   result>0 : 설정된 레이어 총 갯수 반환.
    -   result==0 : 등록된 레이어 없음.
-   Sample
    -   the function setSplitScreen 참조.
    -   [Sandbox_Screen Split](https://sandbox.egiscloud.com/code/main.do?id=effect_screen_split)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getOption().setTwoSlideScreenLayerList("Left_Layer_1,Left_Layer_2", "Right_Layer_1");
```

{% endtab %}
{% endtabs %}

### setTextureCapacityLimit(limit)

> 텍스처 용량 제한 사용 여부를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                  |
| ----- | ------- | -------------------------------------------- |
| limit | boolean | <p>true: 제한 사용<br>false: 제한 미사용</p> |

- Return  
  - 없음.

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getOption().setTextureCapacityLimit(true);
// 또는
Module.getOption().setTextureCapacityLimit(false);
```
{% endtab %}
{% endtabs %}

### setPickingCalculateType(type) → boolean

> 오브젝트 선택(Picking) 처리 시 계산 방식을 설정합니다.
>
> 선택 가능한 방식은 다음과 같습니다:
>
> - `0`: Ray 방식 (기본값)
> - `1`: Color Map 방식

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                                |
| ---- | ------ | ------------------------------------------ |
| type | number | <p>0: Ray 방식<br>1: Color Map 방식</p>     |

- Return  
  - true: 설정 성공  
  - false: 지도 로드 실패 또는 설정 실패

{% endtab %}
{% tab title="Template" %}
```javascript
// Ray 기반 Picking 사용
Module.getOption().setPickingCalculateType(0);

// Color Map 기반 Picking 사용
Module.getOption().setPickingCalculateType(1);
```
{% endtab %}
{% endtabs %}

### setMaxRequestTileMeshSize(size)

> 타일 메시 요청 시 동시에 처리할 최대 요청 개수를 설정합니다.
>
> 값이 0보다 작으면 0으로, 50보다 크면 50으로 자동 조정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                              |
| ---- | ------ | ---------------------------------------- |
| size | number | 동시에 처리할 타일 메시 요청 최대 개수. |

- 설정 가능한 범위: 0 ~ 50

{% endtab %}
{% tab title="Template" %}
```javascript
// 최대 20개까지 타일 메시 요청 처리
Module.getOption().setMaxRequestTileMeshSize(20);
```
{% endtab %}
{% endtabs %}

### setAtmosphericSunriseTime(hour, minute)

> 대기 효과 적용 시 일출 시간을 설정합니다.
>
> 태양 위치 연산에 사용되며, 시각은 24시간제로 입력합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| hour   | number | 일출 시(hour). 0~23 |
| minute | number | 일출 분(minute). 0~59 |

- 유효하지 않은 시간 값은 무시됩니다.
- 대기광 효과가 활성화된 상태에서 적용됩니다.

{% endtab %}
{% tab title="Template" %}
```javascript
// 일출 시간을 오전 6시 30분으로 설정
Module.getOption().setAtmosphericSunriseTime(6, 30);
```
{% endtab %}
{% endtabs %}

### setAtmosphericSunsetTime(hour, minute)

> 대기 효과 적용 시 일몰 시간을 설정합니다.
>
> 태양 위치 연산에 사용되며, 시각은 24시간제로 입력합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description       |
| ------ | ------ | ----------------- |
| hour   | number | 일몰 시(hour). 0~23 |
| minute | number | 일몰 분(minute). 0~59 |

- 유효하지 않은 시간 값은 무시됩니다.
- 대기광 효과가 활성화된 상태에서 적용됩니다.

{% endtab %}
{% tab title="Template" %}
```javascript
// 일몰 시간을 오후 7시 15분으로 설정
Module.getOption().setAtmosphericSunsetTime(19, 15);
```
{% endtab %}
{% endtabs %}

### setAtmosphericTime(hour, minute)

> 대기 효과 적용 시 현재 시간을 설정하여 하늘 색상 변화를 조정합니다.
>
> 설정된 시간은 일출/일몰 및 하늘 색상 변화에 영향을 줍니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description          |
| ------ | ------ | -------------------- |
| hour   | number | 현재 시각(hour), 0~23 |
| minute | number | 현재 분(minute), 0~59 |

- 유효하지 않은 시간 값은 무시됩니다.
- 대기광 효과가 활성화된 상태에서 적용됩니다.
- 일출(`setAtmosphericSunriseTime`) / 일몰(`setAtmosphericSunsetTime`) 시간과 함께 사용하면 하늘 색상 전환 효과를 더 자연스럽게 조절할 수 있습니다.

{% endtab %}
{% tab title="Template" %}
```javascript
// 현재 시각을 오후 4시 30분으로 설정
Module.getOption().setAtmosphericTime(16, 30);
```
{% endtab %}
{% endtabs %}
