import { useEffect, useState } from 'react'
import programs from './assets/student_programs.json'

const List = () => {

    const [data, setData] = useState(null)

    const renderList = () => {
        return(
            data.map(
                (item) => {
                    return(
                        <div className='col-md-4 col-6'>
                            <div className='item-card'>
                                <h3>
                                    {item["Program Name"]}
                                </h3>
                                <p>
                                    {item["Description "]}
                                </p>
                                <a className='explore-btn' href={item["Apply Link"]}>
                                    Explore
                                </a>
                            </div>
                        </div>
                    )
                }
            )
        )
    }

    useEffect((()=>{
        setData(programs.Programs)
    }), [])


    return(
        <div className='list'>
            <div className='row'>
                {data?renderList():null}
            </div>
        </div>
    )
}

export default List